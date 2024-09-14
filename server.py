# server.py
import cv2
import numpy as np
from flask import Flask
from flask_socketio import SocketIO
  # Assume you have a module for object detection

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('video_frame')
def handle_frame(data):
    # Decode the frame
    frame = cv2.imdecode(np.frombuffer(data['frame'], dtype=np.uint8), cv2.IMREAD_COLOR)

    # Encode and send the processed frame back to the client
    _, buffer = cv2.imencode('.jpg', frame)
    socketio.emit('processed_frame', {'frame': buffer.tobytes()})

@app.route('/')
def index():
    return "Server is running."

if __name__ == '__main__':
    socketio.run(app, port=5000, allow_unsafe_werkzeug=True)
