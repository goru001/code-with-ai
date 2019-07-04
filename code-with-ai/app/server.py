from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import uvicorn, aiohttp, asyncio
from io import BytesIO

from config import config
from fastai.text import *

path = Path(__file__).parent
id_to_col = []
setup_done = False
learn = None

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory=path/'static'))

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

async def setup_learner():
    global learn
    await download_file(config.model_file_url, path/'models'/f'{config.model_file_name}')
    await download_file(config.data_file_url, path /'data'/ f'{config.data_file_name}')
    await download_file(config.vocabulary_file_url, path /'data'/ f'{config.vocabulary_file_name}')
    await download_file(config.id_to_col_url , path / 'data' / f'{config.id_to_col_file_name}')
    with open(path / 'data'/ f'{config.vocabulary_file_name}', 'rb') as f:
        vocabulary = pickle.load(f)
    global id_to_col
    with open(path / 'data'/'id_to_col.pkl', 'rb') as f:
        id_to_col = pickle.load(f)
    label_cols = list(range(1, 94))
    data_clas = TextClasDataBunch.from_csv(path=path, csv_name='data/competitive_cleaned.csv', vocab=vocabulary,
                                           text_cols=[0], label_cols=label_cols)
    learn = text_classifier_learner(data_clas, drop_mult=0.5)
    learn.load('competitive')
    return learn

# async def setup():
#     global learn, setup_done
#     loop = asyncio.get_event_loop()
#     tasks = [asyncio.ensure_future(setup_learner())]
#     learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
#     loop.close()
#     setup_done = True


@app.route('/')
def index(request):
    html = path/'view'/'index.html'
    return HTMLResponse(html.open().read())

@app.route('/analyze', methods=['POST'])
async def analyze(request):
    global setup_done, learn
    if not setup_done:
        learn = await setup_learner()
        setup_done = True
    data = await request.form()
    problem_statement = data['problem']
    print(problem_statement)
    if len(problem_statement) > 0:
        pred = learn.predict(problem_statement)
        above_thresh = (pred[2].numpy() > 0.2)
        result = [[id_to_col[i + 1], int(pred[2].numpy()[i]*100)] for i, x in enumerate(above_thresh) if x]
    else:
        result = []
    return JSONResponse({'result': result})

if __name__ == '__main__':
    if 'serve' in sys.argv: uvicorn.run(app, host='0.0.0.0', port=8080)

