import sys
from flask import Flask, render_template, Response
from webcamvideostream import WebcamVideoStream
import time
import threading

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'pi'
app.config['BASIC_AUTH_PASSWORD'] = 'pi'
app.config['BASIC_AUTH_FORCE'] = True

last_epoch = 0


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pir')
def pir():
    return render_template('pir.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)