import sys
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import json
import requests
import time
import pika
import logging


app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)


log = logging.getLogger('spam_application')
log.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
ch.setFormatter(formatter)
log.addHandler(ch)



@app.route("/hello")
def hello():
    return "Hello CHEESE!"



@app.route("/upload")
def upload():
    return render_template('index.html')



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'