import time
import traceback

import RPi.GPIO as GPIO


class LED:
    def __init__(self, channel, frequency):
        """
        `channel`: PIN number

        `frequency`: frequency in Hz
        """
        self._PIN = channel
        GPIO.setup(self._PIN, GPIO.OUT)
        self._PWM = GPIO.PWM(self._PIN, frequency)

    def start(self, duty_cycle):
        """
        `duty_cycle` must have a value from `0.0` to `1.0`
        """
        self._PWM.start(duty_cycle)

    def stop(self):
        self._PWM.stop()


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)

    LED_1 = 5
    LED_2 = 6
    LED_3 = 13

    l1 = LED(LED_1, 10)
    l2 = LED(LED_2, 50)
    l3 = LED(LED_3, 100)

    l1.start(0.5)
    l2.start(0.5)
    l3.start(0.5)

    input('Enter to exit')
    GPIO.cleanup()
