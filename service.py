from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import json
import proto_csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/uploader", methods = ['POST'])
def uploader():
        f = request.files['file']
        f.save(secure_filename(f.filename))
        states, data = proto_csv.parse(f.filename)

        print(states)
        print("############")
        print(data)

        return render_template('index.html', states=states, data=json.dumps(data))


if __name__ == '__main__':
   app.run(debug = True)


