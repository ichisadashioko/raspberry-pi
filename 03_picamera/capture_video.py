from picamera import PiCamera
import time


def time_now():
    return time.strftime('%Y-%m-%d_%H-%M-%S', time.gmtime())


camera = PiCamera()

camera.start_preview()
camera.start_recording('{}.h264'.format(time_now()))
time.sleep(10)
camera.stop_recording()
camera.stop_preview()