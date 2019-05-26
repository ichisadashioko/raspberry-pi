import time

import RPi.GPIO as GPIO

import control_utils as cu

if __name__ == "__main__":
    # Components
    # - Raspberry Pi Model B+ (Pi)
    # - L298N Motor Controller (L298N)
    # - 2x DC 6V motors
    # - 4x 1.2V AA batteries
    #
    # Wiring
    # - 4.8V+ (Power supply) <-> VCC (L298N)
    # 3v3 Power 17 (Pi) <-> 5V (L298N)
    # - 4.8V-(Power supply) <-> GRN (L298N) <-> 330 Ohms resistor <-> Ground 39 (Pi)
    # - IN1 (L298N) <-> BCM_5 (Pi)
    # - IN2 (L298N) <-> BCM_6 (Pi)
    # - IN3 (L298N) <-> BCM_17 (Pi)
    # - IN4 (L298N) <-> BCM_27 (Pi)

    GPIO.setmode(GPIO.BCM)

    IN1 = 5
    IN2 = 6
    IN3 = 17
    IN4 = 27

    controller = cu.L298N(IN1, IN2, IN3, IN4)

    try:
        while True:
            cmd = input('Enter command (up, down, left, right, exit):')

            if cmd == 'up':
                controller.forward()
                time.sleep(0.5)
                controller.stop()
            elif cmd == 'down':
                controller.backward()
                time.sleep(0.5)
                controller.stop()
            elif cmd == 'left':
                controller.left()
                time.sleep(0.5)
                controller.stop()
            elif cmd == 'right':
                controller.right()
                time.sleep(0.5)
                controller.stop()
            elif cmd == 'exit':
                break
    except:
        pass

    controller.stop()
    GPIO.cleanup()
