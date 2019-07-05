# Code with AI
Code with AI is a tool which predicts which techniques one should use to solve a competitive programming problem to get an AC

Tool: https://code-with-ai.app.render.com/

Usage:

1. Copy paste the problem statement
2. Hit Enter :)


![Alt Text](code-with-ai/app/static/images/code-with-ai.gif)


* This tool was very well received by competitive programming community. Check out my blog post on codeforces [here](https://codeforces.com/blog/entry/64604)

* This tool was also shared by Jeremy Howard on Twitter. Check out his [tweet](https://twitter.com/jeremyphoward/status/1088432121595650048).

* Some Analytics: [3300+ unique users](https://drive.google.com/open?id=1IqlUlQmGPAk4iNc7Yv6T8wx9LNTcCyhd) have used this tool, till June 2019 since its launch.

## Dataset

I scraped the dataset from Codechef and Codeforces, the scripts for which along with the dataset you can find in `ulmfit-model/competitive-programming-websites-scripts`


The dataset on which model has been trained has 92 classes, which are: 

`'mobius-function',
 'queue',
 'greedy',
 'suffix-array',
 'bitmasks',
 'digit dp',
 'lca',
 'gcd',
 'probabilities',
 'combinatorics',
 'graph matchings',
 'easy-medium',
 'precomputation',
 'sprague-grundy',
 'math',
 'centroid-decomposition',
 'link-cut-tree',
 'expression parsing',
 'constructive algorithms',
 'medium',
 'schedules',
 'euler tour',
 'easy',
 'challenge',
 'implementation',
 'binary search',
 'matrices',
 'two pointers',
 'dfs',
 'dp+bitmask',
 'sets',
 'sqrt-decomposition',
 'dijkstra',
 'line-sweep',
 'data structures',
 'tree-dp',
 'hard',
 'mst',
 'recursion',
 'games',
 'suffix-trees',
 'kmp',
 'stack',
 'brute force',
 'medium-hard',
 'prefix-sum',
 'graphs',
 '2-sat',
 'shortest paths',
 'heavy-light',
 'heaps',
 '*special problem',
 'trees',
 'array',
 'sliding-window',
 'inclusion-exclusion',
 'meet-in-the-middle',
 'dfs and similar',
 'sortings',
 'pigeonhole',
 'xor',
 'gaussian-elimination',
 'lucas theorem',
 'divide and conquer',
 'flows',
 'strings',
 'matrix-expo',
 'number theory',
 'bipartite',
 'knapsack',
 'sieve',
 'ternary search',
 'modulo',
 'backtracking',
 'treap',
 'trie',
 'dp',
 'fenwick',
 'observation',
 'fibonacci',
 'convex-hull',
 'chinese remainder theorem',
 'string suffix structures',
 'geometry',
 'lazy propagation',
 'factorization',
 'dsu',
 'fft',
 'segment-tree',
 'hashing',
 'bfs',
 'prime',
 'mo algorithm'`
 
 These classes are a union of tags which codeforces and codechef have! You can check out more details about data preparation in `ulmfit-model/code-with-ai-data-preparation.ipynb`

## Model

You can check out the code for model in notebook `ulmfit-model/code-with-ai.ipynb`

Basically, the classifier is built starting from `Wikitext103` Language Model pretrained weights,
fine-tuning the language model on current dataset and then building classifier on
top of fine-tuned language model.

## Results

The classifier has a F1 Score of ~49.

## TODOs

* Try improving the score further by using bidirectional RNN
 
* Try improving the score further by using an approach similar to [DeViSE](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41473.pdf) paper, i.e instead of training the model to predict O or 1, train the model to go closer towards the embedding vector representation of labels - the intuition behind this is that labels in competitive programming like graph, dfs, bfs etc aren’t disjoint.
