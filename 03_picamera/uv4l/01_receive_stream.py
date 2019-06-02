import numpy as np
import cv2

if __name__ == "__main__":
    stream_url = 'http://raspberrypi.local:8080/stream/video.mjpeg'
    cap = cv2.VideoCapture()
    cap.open(stream_url)

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)

            k = cv2.waitKey(1) & 0xff

            if k == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()