


"""
nokogiri@nokogiri:~/l7_homework/takehome$


docker build . 
docker compose up

127.0.0.1:8000/hello
http://10.0.0.25:8000/hello


## local run
export FLASK_APP=app.py
flask run

https://pythonbasics.org/flask-upload-file/
werkzeug


psuedocode:
HTML accepts file 
were not going to do any validating. Only throwing errors if not perfect. Writing to log.
ingest / split file 
find column of interest
build into some format 
spit data back to frontend JS 
populate charts with highcharts



https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/column-rotated-labels



"""



"""
#### Part 1
>> ingest the attached example file

So we need to sort out which columns which might be which.

How complex is the total solution space? If theres no structures to the files -- we start in the extremes.

First off we should dump any errors -- so if were ingesting something that fails, well we have an example of WHAT failure happened.

We should test one of the columns to see if it matches against a known-true solution: EX: States explitic, and State abbreviated.

Im not exactly sure what this data in these columns should be....

csv file is tab delimited 

OK so HOW to present this data, there are towns, there are states ...
Do I want to group by state?
Do i want categories within states per town?

So we have 20-thousand lines -- do I want to know how many towns per state?

Say 50 states ... 20,000/50 = 400 cities per state. COULD graph this but we wont.

SO lets just lump all the populations together within each state. We will still have 10 graphs per 50 states.

So the drill down column is perfect.

https://www.highcharts.com/demo/column-drilldown
https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/column-drilldown

## this might be a better way to present it...
https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/bar-stacked


http://jsfiddle.net/pawel_dalek/oLme65xs/





"""

OK so we need TWO sets of data.
***** THE LANDING CHART

[
    {
        name: 'Chrome',
        y: 63.06,
        drilldown: 'Chrome'
    },
    {
        name: 'Safari',
        y: 19.84,
        drilldown: 'Safari'
    },
...
    {
        name: 'Other',
        y: 1.582,
        drilldown: null
    }
]



so then top_level_data is a list of dicts 

where EXAMPLE dict: 
    {
        name: 'Chrome',
        y: 63.06,
        drilldown: 'Chrome'
    }
where OUR dict: 
    {
        name: 'Alabama',
        y: 63.06,
        drilldown: 'Alabama'
    }



***** THE DRILL-DOWN DATA ... within each ... this will be the prevalence of 0-9
LIST of dictionaries...
EACH dict:
{name:, X, id: Y, data: []}
... where the final list looks like:
    ['v65.0',0.1],
    ['v64.0',1.3],
    ['v63.0',53.02],

SO for OUR data it will be INSTEAD:
    ['0',0],
    ['1',120],
    ['2',10],
    ['3',3],



series: [
    {
        name: 'Chrome',
        id: 'Chrome',
        data: ['v65.0',0.1],['v64.0',1.3],['v63.0',53.02],['v62.0',1.4],['v61.0',0.88],['v60.0',0.56],
            ['v59.0',0.45],['v58.0',0.49],['v57.0',0.32],['v56.0',0.29],['v55.0',0.79],['v54.0',0.18],
            ['v51.0',0.13],['v49.0',2.16],['v48.0',0.13],['v47.0',0.11],['v43.0',0.17],['v29.0',0.26]
    },
    {
        name: 'Firefox',
        id: 'Firefox',
        data: [
            [
                'v58.0',
                1.02
            ],
            [
                'v57.0',
                7.36
            ],
...
            [
                'v47.0',
                0.12
            ]
        ]
    },
    {
        name: 'Internet Explorer',
        id: 'Internet Explorer',
        data: [
            [
                'v11.0',
                6.2
            ],
            [
                'v10.0',
                0.29
            ],
            [
                'v9.0',
                0.27
            ],
            [
                'v8.0',
                0.47
            ]
        ]
    },
    {
        name: 'Safari',
        id: 'Safari',
        data: [
            [
                'v11.0',
                3.39
            ],
            [
                'v10.1',
                0.96
            ],
            [
                'v10.0',
                0.36
            ],
            [
                'v9.1',
                0.54
            ],
            [
                'v9.0',
                0.13
            ],
            [
                'v5.1',
                0.2
            ]
        ]
    },
    {
        name: 'Edge',
        id: 'Edge',
        data: [
            [
                'v16',
                2.6
            ],
            [
                'v15',
                0.92
            ],
            [
                'v14',
                0.4
            ],
            [
                'v13',
                0.1
            ]
        ]
    },
    {
        name: 'Opera',
        id: 'Opera',
        data: [
            [
                'v50.0',
                0.96
            ],
            [
                'v49.0',
                0.82
            ],
            [
                'v12.1',
                0.14
            ]
        ]
    }
]



"""

#### Part 2
>> validates Benford’s assertion based on the '7_2009' column in the supplied file

I dont know what exactly this column is... so how are we going to detect for it... so I might need more data.

It SAYS its a 'census' ...so we assume population?

I suppose I could just graph all 3 and just roll the dice on everything?


"""





"""
#### Part 3
> graph of the observed distribution of numbers






"""







