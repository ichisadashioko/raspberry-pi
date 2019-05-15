from picamera import PiCamera
import time


def time_now():
    return time.strftime('%Y-%m-%d_%H-%M-%S', time.gmtime())


camera = PiCamera()

camera.start_preview()
time.sleep(5)
camera.capture('{}.png'.format(time_now()))
camera.stop_preview()
