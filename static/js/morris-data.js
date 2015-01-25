$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2010 Q1',
            health: 2666,
            safety: null,
            education: 2647
        }, {
            period: '2010 Q2',
            health: 2778,
            safety: 2294,
            education: 2441
        }, {
            period: '2010 Q3',
            health: 4912,
            safety: 1969,
            education: 2501
        }, {
            period: '2010 Q4',
            health: 3767,
            safety: 3597,
            education: 5689
        }, {
            period: '2011 Q1',
            health: 6810,
            safety: 1914,
            education: 2293
        }, {
            period: '2011 Q2',
            health: 5670,
            safety: 4293,
            education: 1881
        }, {
            period: '2011 Q3',
            health: 4820,
            safety: 3795,
            education: 1588
        }, {
            period: '2011 Q4',
            health: 15073,
            safety: 5967,
            education: 5175
        }, {
            period: '2012 Q1',
            health: 10687,
            safety: 4460,
            education: 2028
        }, {
            period: '2012 Q2',
            health: 8432,
            safety: 5713,
            education: 1791
        }],
        xkey: 'period',
        ykeys: ['health', 'education', 'safety'],
        labels: ['health', 'education', 'safety'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Download Sales",
            value: 12
        }, {
            label: "In-Store Sales",
            value: 30
        }, {
            label: "Mail-Order Sales",
            value: 20
        }],
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '2006',
            a: 100,
            b: 90
        }, {
            y: '2007',
            a: 75,
            b: 65
        }, {
            y: '2008',
            a: 50,
            b: 40
        }, {
            y: '2009',
            a: 75,
            b: 65
        }, {
            y: '2010',
            a: 50,
            b: 40
        }, {
            y: '2011',
            a: 75,
            b: 65
        }, {
            y: '2012',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true
    });

});
