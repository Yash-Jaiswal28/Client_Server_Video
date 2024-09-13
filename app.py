from flask import Flask,render_template,Response
import cv2
from ultralytics import YOLO

app=Flask(__name__)
camera=cv2.VideoCapture(0)

# Load the YOLOv8 model
model = YOLO("yolov8l.pt")

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def gen_detect():
    # Initialize video capture (0 for default camera, change index if needed)
    while True:
        ret, frame = camera.read()
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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_detect')
def video_detect():
     return Response(gen_detect(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=="__main__":
    app.run(debug=True)
