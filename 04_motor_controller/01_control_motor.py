import time

import RPi.GPIO as GPIO
# import gpiozero
# from gpiozero import Motor


# m1 = Motor(M1_IN1, M1_IN2)
# m2 = Motor(M2_IN3, M2_IN3)

# m1.backward()

# time.sleep(1)

# m1.forward()
# m2.forward()

# time.sleep(1)

# m1.stop()
# m2.stop()


class Motor:
    def __init__(self, forward, backward):
        self._forward = forward
        self._backward = backward
        GPIO.setup(self._forward, GPIO.OUT)
        GPIO.setup(self._backward, GPIO.OUT)

    def forward(self):
        GPIO.output(self._backward, False)
        GPIO.output(self._forward, True)

    def backward(self):
        GPIO.output(self._forward, False)
        GPIO.output(self._backward, True)

    def stop(self):
        GPIO.output(self._forward, False)
        GPIO.output(self._backward, False)


class MotorController:
    def __init__(self, in1, in2, in3, in4):
        self.motor1 = Motor(in1, in2)
        self.motor2 = Motor(in3, in4)

    def forward(self):
        self.motor1.forward()
        self.motor2.forward()

    def backward(self):
        self.motor1.backward()
        self.motor2.backward()

    def left(self):
        self.motor1.backward()
        self.motor2.forward()

    def right(self):
        self.motor1.forward()
        self.motor2.backward()

    def stop(self):
        self.motor1.stop()
        self.motor2.stop()


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    M1_IN1 = 25
    M1_IN2 = 8
    M2_IN3 = 7
    M2_IN4 = 1

    m_controller = MotorController(M1_IN1, M1_IN2, M2_IN3, M2_IN4)

    m_controller.left()

    time.sleep(2)

    m_controller.stop()

    GPIO.cleanup()
