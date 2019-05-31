import time

import RPi.GPIO as GPIO


class UltrasonicSensor:
    def __init__(self, trigger: int, echo: int):
        """
        `trigger`: trigger pin number

        `echo`: echo pin number
        """
        self._TRIG = trigger
        self._ECHO = echo
        self.speed_of_sound = 343.26  # m/s
        self.max_distance = 4.0  # m
        self.min_distance = 0.02  # m

        GPIO.setup(self._TRIG, GPIO.OUT)
        GPIO.setup(self._ECHO, GPIO.IN)

    def send_and_receive(self):
        GPIO.output(self._TRIG, True)
        time.sleep(0.00001)  # 100us or 1e-4 seconds
        GPIO.output(self._TRIG, False)
        # Wait up to 100ms for the echo pin to rise and fall (25ms is the maximum pulse time,
        # but the pre-rise time is unspecified in the "datasheet".
        # 100ms seems sufficiently long to conclude something has failed)

        start_time = 0
        sig_time = 0
        while GPIO.input(self._ECHO) == False:
            start = time.time()

        while GPIO.input(self._ECHO) == True:
            sig_time = time.time() - start

        return sig_time

    def calculate_distance(self):
        sig_time = self.send_and_receive()

        d = self.speed_of_sound * sig_time / 2

        if d < self.min_distance:
            d = 0
        elif d > self.max_distance:
            d = -1
        return d
