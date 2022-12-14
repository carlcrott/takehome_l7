import sys
from flask import Flask, request
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
