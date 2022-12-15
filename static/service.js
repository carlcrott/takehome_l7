




$(document).ready(function(){



    // $('#sequence_submit').on( "click", dnaSeqPost );

    // $.ajax({
    //     type: "POST",
    //     contentType: "application/json; charset=utf-8",
    //     url: "http://localhost:1234/rev_comp/",
    //     data: JSON.stringify(jsonSeq),
    //     success: function(response) {
    //         $('#output_text').text(response);

    //         $('#validation_text').html(sequence+"<br/>"+response.split("").reverse().join(""));
    //     },
    // });

    /*
    check ID data_output for correctly parsible JSON.

    if json parses correctly ... run highcharts.


    How does highcharts want the data formatted?
    */






    if ( $('#data_output').html().trim() != "" ) {
        // alert("DATA FILLED");
    } else {
        // alert("EMPTY");
    };


// Data retrieved from https://gs.statcounter.com/browser-market-share#monthly-202201-202201-bar


// // EXAMPLE VERSION
// Highcharts.chart('container', {
//     chart: {
//         type: 'bar'
//     },
//     title: {
//         text: 'UEFA CL most assists by season'
//     },
//     xAxis: {
//         categories: ['2021/22', '2020/21', '2019/20', '2018/19', '2017/18']
//     },
//     yAxis: {
//         min: 0,
//         title: {
//             text: 'Assists'
//         }
//     },
//     tooltip: {
//         pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
//         shared: true
//     },
//     plotOptions: {
//         bar: {
//             stacking: 'percent'
//         }
//     },
//     series: [{
//         name: 'Kevin De Bruyne',
//         data: [4, 4, 2, 4, 4]
//     }, {
//         name: 'Joshua Kimmich',
//         data: [0, 4, 3, 2, 3]
//     }, {
//         name: 'Sadio Mané',
//         data: [1, 2, 2, 1, 2]
//     }]
// });

///////////////////////////////////////////////////////////////

// // IMPLEMENTATION VERSION
// MODELED AFTER: http://jsfiddle.net/pawel_dalek/oLme65xs/

// Highcharts.chart('container', {
//     chart: {
//         type: 'bar'
//     },
//     title: {
//         text: 'Benfords Law'
//     },
//     xAxis: {
//         categories: ['Alabama', 'Texas', 'Wyoming']
//     },
//     yAxis: {
//         min: 0,
//         title: {
//             text: 'First number of population'
//         }
//     },
//     tooltip: {
//         pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
//         shared: true
//     },
//     plotOptions: {
//         bar: {
//             stacking: 'percent'
//         }
//     },

/* 
TOP LEVEL LIST will be 10 items long ... 1,2,3,4,5,6,7,8,9,0

THE INDIVIDUAL dicts in this series 
... will each be 50 items long and be Alabama through Wyoming
... and there will be 9 series of data.
*/

//     series: [{
//         name: 'Integer 1',
//         data: [4, 4, 2, 4, 4]
//     }, {
//         name: 'Integer 2',
//         data: [0, 4, 3, 2, 3]
//     }, {
//         name: 'Integer 3',
//         data: [1, 2, 2, 1, 2]
//     }]
// });





})