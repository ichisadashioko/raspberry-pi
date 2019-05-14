import time
import traceback

import RPi.GPIO as GPIO

# use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

LED_PIN = 4

GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        action = str(input('Enter action (high, low, exit):'))

        if action == 'high':
            GPIO.output(LED_PIN, GPIO.HIGH)
        elif action == 'low':
            GPIO.output(LED_PIN, GPIO.LOW)
        elif action == 'exit':
            GPIO.cleanup()
            break
        else:
            pass

except:
    GPIO.cleanup()
    traceback.print_stack()
