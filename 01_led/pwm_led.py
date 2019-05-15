import time
import traceback

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED_PIN = 4

GPIO.setup(LED_PIN, GPIO.OUT)
p = GPIO.PWM(LED_PIN, 50)

p.start(0)

try:
    while True:
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100):
            p.ChangeDutyCycle(100 - i)
            time.sleep(0.02)
except:
    p.stop()
    GPIO.cleanup()
    traceback.print_exc()
