import time

import RPi.GPIO as GPIO


class Motor:
    def __init__(self, forward, backward):
        """
        `forward`: PIN number

        `backward`: PIN number
        """
        self._forward = forward
        self._backward = backward
        GPIO.setup(self._forward, GPIO.OUT)
        GPIO.setup(self._backward, GPIO.OUT)

    def forward(self):
        print('Turning on GPIO', self._forward)
        GPIO.output(self._forward, True)
        print('Turning off GPIO', self._backward)
        GPIO.output(self._backward, False)

    def backward(self):
        print('Turning off GPIO', self._forward)
        GPIO.output(self._forward, False)
        print('Turning on GPIO', self._backward)
        GPIO.output(self._backward, True)

    def stop(self):
        print('Turning off GPIO', self._forward)
        GPIO.output(self._forward, False)
        print('Turning off GPIO', self._backward)
        GPIO.output(self._backward, False)


class L298N:
    def __init__(self, in1, in2, in3, in4):
        self.motor_a = Motor(in1, in2)
        self.motor_b = Motor(in3, in4)

    def forward(self):
        self.motor_a.forward()
        self.motor_b.forward()

    def backward(self):
        self.motor_a.backward()
        self.motor_b.backward()

    def left(self):
        self.motor_a.forward()
        self.motor_b.backward()

    def right(self):
        self.motor_a.backward()
        self.motor_b.forward()

    def stop(self):
        self.motor_a.stop()
        self.motor_b.stop()

    def all(self):
        GPIO.output(self.motor_a._forward, True)
        GPIO.output(self.motor_a._backward, True)
        GPIO.output(self.motor_b._forward, True)
        GPIO.output(self.motor_b._backward, True)
