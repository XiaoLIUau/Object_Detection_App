import cv2


def camera():
    # Initialize the camera (0 is the default camera)
    return cv2.VideoCapture(0)


def text_display(frame,text):
    # Add text to the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_position = (round(frame.shape[1]- 1000), 100) #(round(frame.shape[1]/2), frame.shape[0] - 10)  # Adjust '100' and '10' for exact positioning
    cv2.putText(frame, text, text_position, font, 3, (0, 0, 0), 2, cv2.LINE_AA)
    return


def video_display(frame,text):
    # Add text to display video
    text_display(frame,text)
    # Display the resulting frame
    cv2.imshow('Camera Stream', frame)
    return