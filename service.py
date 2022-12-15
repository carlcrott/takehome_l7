import sys
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import json
import requests
import time
import pika
import logging
import proto_csv

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)


@app.route("/hello")
def hello():
    return "Hello CHEESE!"


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/uploader", methods = ['POST'])
def uploader():
        f = request.files['file']
        f.save(secure_filename(f.filename))

        # proto_csv.parse(f.filename)

        # asdf = open('census_2009b.csv','r')
        # asdf = open(f.filename,'r')
        states, data = proto_csv.parse(f.filename)

        print(states)
        print("############")
        print(data)

        output_json = {}
        output_json['states'] = states
        output_json['data'] = data

        # output_json


        # Do we delete here? IDK. 
        # What happens re-uploads / overwriting?
        return render_template('index.html', states=states, data=json.dumps(data))




if __name__ == '__main__':
   app.run(debug = True)


