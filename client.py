# client.py
import cv2
import socketio
import numpy as np

# Connect to the Flask server via WebSockets
sio = socketio.Client()

@sio.event
def connect():
    print('Connected to the server')

@sio.event
def disconnect():
    print('Disconnected from the server')

@sio.on('receive_frame')
def receive_frame(data):
    # Convert the processed frame received from the server and display
    frame = cv2.imdecode(np.frombuffer(data['frame'], dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow('Processed Video Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sio.disconnect()

def stream_video():
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Encode frame to send over the network
        _, buffer = cv2.imencode('.jpg', frame)
        sio.emit('video_frame', {'frame': buffer.tobytes()})

        cv2.imshow('Original Video Stream', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:5000')  # Replace with your server's address
    stream_video()
