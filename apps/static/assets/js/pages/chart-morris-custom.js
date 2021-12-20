'use strict';
$(document).ready(function() {
    setTimeout(function() {
    // [ bar-simple ] chart start
    Morris.Line({
        element: 'morris-line-chart',
        data: [{
            y: '2006',
            a: 20,
            b: 10
        },
        {
            y: '2007',
            a: 55,
            b: 45
        },
        {
            y: '2008',
            a: 45,
            b: 35
        },
        {
            y: '2009',
            a: 75,
            b: 65
        },
        {
            y: '2010',
            a: 50,
            b: 40
        },
        {
            y: '2011',
            a: 75,
            b: 65
        },
        {
            y: '2012',
            a: 100,
            b: 90
        }
        ],
        xkey: 'y',
        redraw: true,
        resize: true,
        smooth: false,
        ykeys: ['a', 'b'],
        hideHover: 'auto',
        responsive:true,
        labels: ['Series A', 'Series B'],
        lineColors: ['#1de9b6', '#04a9f5']
    });
    }, 700);
});
