from flask_socketio import *
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

if __name__ == '__main__':
    socketio.run(app, debug=True)
    

@socketio.on('connect')
def connected():
    print('Connected')
    emit('Connection etablished' , {'coonect' : True} , broadscat=True)

@socketio.on('disconnect')
def disconnected():
    print('Disconnected')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return f.filename

@socketio.on('AnalyzeVideo')
def userAdded(message):
    print(message)
 
@app.route("/")
def index():
    return "Hello world"



