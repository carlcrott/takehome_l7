




$(document).ready(function(){


    if ( $('#data_output').html().trim() != "" ) {
        // alert("DATA FILLED");
        var asdf = $('#states_output').html().trim();
        var states = asdf.substring(1, asdf.length-1).split(",");

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
            subtitle: {
                text: 'In 1938, Frank Benford published a paper showing the distribution of the leading digit in many disparate sources of data. \n In all these sets of data, the number 1 was the leading digit about 30% of the time.'
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