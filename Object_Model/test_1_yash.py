from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# Load the YOLOv8 model
model = YOLO("yolov8l.pt")

@app.route('/')
def index():
    return render_template('index_1.html')

def gen_frames():
    # Initialize video capture (0 for default camera, change index if needed)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Resize frame for faster processing
        frame = cv2.resize(frame, (640, 480))

        # Run YOLO model to detect objects in the frame
        results = model.predict(frame)

        # Annotate the frame with predictions
        annotated_frame = results[0].plot()

        # Encode the annotated frame to a format suitable for streaming
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # Yield the frame as a stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    # Streaming the video
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
