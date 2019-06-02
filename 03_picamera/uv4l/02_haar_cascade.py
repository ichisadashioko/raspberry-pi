import time

import numpy as np
import cv2

def time_now():
    return time.strftime('%H:%M:%S', time.gmtime())

if __name__ == "__main__":
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    stream_url = 'http://raspberrypi.local:8080/stream/video.mjpeg'
    cap = cv2.VideoCapture()
    cap.open(stream_url)

    while True:
        ret, frame = cap.read()
        if ret:

            start_time = time.time()

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            faces = face_cascade.detectMultiScale(
                image=gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                print(f'{time_now()} detect face at [{x}, {y}]')
                cv2.rectangle(
                    img=frame,
                    pt1=(x, y),
                    pt2=(x + w, y + h),
                    color=(255, 0, 0),
                    thickness=2,
                )

            eyes = eye_cascade.detectMultiScale(gray)
            for (ex, ey, ew, eh) in eyes:
                print(f'{time_now()} detect eye at [{ex}, {ey}]')
                cv2.rectangle(
                    img=frame,
                    pt1=(ex, ey),
                    pt2=(ex + ew, ey + eh),
                    color=(0, 255, 0),
                    thickness=2,
                )

            delay = time.time() - start_time

            cv2.putText(
                img=frame,
                text=f'{delay:.02}s',
                org=(5, 25),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(0, 255, 0),
                lineType=cv2.LINE_AA,
            )

            cv2.imshow('frame', frame)

            k = cv2.waitKey(1) & 0xff

            if k == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
