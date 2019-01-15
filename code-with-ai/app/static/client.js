var el = x => document.getElementById(x);

function onSuccess(response) {
    if ($('#graph').hasClass('hidden')) {
         $('#graph').removeClass('hidden');
    }

    var begHtml = `<div class="wrap">
                    <div class="holder">`
    var endHtml = `</div>
                </div>`
    var midHtml = ''

    results = response['result']
    if(results.length > 0) {
        for(var i=0; i<results.length; i++) {
            midHtml += '<div class="bar cf" data-percent="' + String(results[i][1]) + '%"style="width: ' + String(results[i][1]) + '%"><span class="label">' + String(results[i][0]) + '</span><span class="count">' + String(results[i][1]) + '%</span></div>'
        }
        var innerHtml = begHtml + midHtml + endHtml;
        $('#graph').html(innerHtml);
    } else {
        // nothing to show
    }

    if (!$('#loading').hasClass('hidden')) {
         $('#loading').addClass('hidden');
    }

}

function analyze() {
    var problem = el('problem').value;
    if (problem.length == 0) alert('Please paste the problem statement');

    if ($('#loading').hasClass('hidden')) {
         $('#loading').removeClass('hidden');
    }

    if (!$('#graph').hasClass('hidden')) {
         $('#graph').addClass('hidden');
    }
    var loc = window.location;
    var url = `${loc.protocol}//${loc.hostname}:${loc.port}/analyze`;
    var data = {
        problem: problem
    }
    $.ajax({
      type: "POST",
      url: url,
      data: data,
      success: onSuccess,
      dataType: "json"
    });
    return false;
}

