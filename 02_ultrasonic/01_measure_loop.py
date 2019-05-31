import sys
import time
import traceback

import RPi.GPIO as GPIO

import ultrasonic
if __name__ == "__main__":
    # use BCM GPIO numbering
    GPIO.setmode(GPIO.BCM)
    # GND = 5th pin top left
    VCC = 17  # 6th pin top left
    TRIG = 27  # 7th pin top left
    ECHO = 22  # 8th pin top left

    timeout = 0.2
    try:
        GPIO.setup(VCC, GPIO.OUT)
        sensor = ultrasonic.UltrasonicSensor(trigger=TRIG, echo=ECHO)
        GPIO.output(VCC, True)

        while True:
            distance = sensor.calculate_distance()

            print('Distance:', distance, 'm')
            time.sleep(timeout)
    except:
        GPIO.cleanup()
        print()
        traceback.print_exc()
