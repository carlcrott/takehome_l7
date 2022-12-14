


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



"""



"""
#### Part 1
>> ingest the attached example file

So we need to sort out which columns which might be which.

How complex is the total solution space? If theres no structures to the files -- we start in the extremes.

First off we should dump any errors -- so if were ingesting something that fails, well we have an example of WHAT failure happened.

We should test one of the columns to see if it matches against a known-true solution: EX: States explitic, and State abbreviated.

Im not exactly sure what this data in these columns should be....

lol OK the csv file is malformed.


"""




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







