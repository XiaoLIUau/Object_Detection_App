import cv2
import requests
# # When main.py located one directory above App folder/package
# from App.DetectionBuffer import *
# from App.prediction import predict_frame, load_model
# from App.camera import camera, video_display
from DetectionBuffer import *
from prediction import predict_frame, load_model
from camera import camera, video_display


def main():
    # setups
    cap = camera()
    print('Loading AI Model')
    model = load_model()
    print('Model Loaded')
    not_flagged_counter = 0 
    action_msg = None
    buffer_size = 3
    buffer = DetectionBuffer(size=buffer_size)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit();

    # Stream each frame
    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame (stream end?). Exiting ...")
                break
            
            # Detect Object
            output = predict_frame(frame, model)
            buffer.add_detection(output)
            not_flagged_counter,action_msg =notification_buffer(buffer,not_flagged_counter)
            if action_msg is not None:
                print(action_msg)
                # send notification
                requests.get('http://localhost:5000/notify')
            
            # Display the resulting frame
            video_display(frame,output)

            # Press 'q' to exit the stream
            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":

    # app.run(debug=True, host='0.0.0.0')
    # requests.get('http://localhost:5000/notify')
    main()
