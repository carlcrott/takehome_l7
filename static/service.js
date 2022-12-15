




$(document).ready(function(){


    if ( $('#data_output').html().trim() != "" ) {
        // alert("DATA FILLED");
        var states = $('#states_output').html().trim().split(",")
        var data = JSON.parse(String($('#data_output').html().trim()));


        // // IMPLEMENTATION VERSION
        // MODELED AFTER: http://jsfiddle.net/pawel_dalek/oLme65xs/
        Highcharts.chart('container', {
            chart: {
                type: 'bar',
                height: '85%',
            },
            title: {
                text: 'Benfords Law'
            },
            xAxis: {
                categories: states
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'First number of population'
                }
            },
            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                shared: true
            },
            plotOptions: {
                bar: {
                    stacking: 'percent'
                }
            },
            series: data
        });





    } else {
        // alert("EMPTY");
    };









})