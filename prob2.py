import RPi.GPIO as GPIO
import time

MotorPinA = 11
MotorPinB = 12
MotorEnablePin = 13
YellowLedPin = 15
RedLedPin = 16

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MotorPinA, GPIO.OUT)
    GPIO.setup(MotorPinB, GPIO.OUT)
    GPIO.setup(MotorEnablePin, GPIO.OUT)
    GPIO.setup(YellowLedPin, GPIO.OUT)
    GPIO.setup(RedLedPin, GPIO.OUT)
    GPIO.output(MotorEnablePin, GPIO.LOW)

def loop():
    try:
        while True:
            print('Press Ctrl+C to end the program...')
            GPIO.output(MotorEnablePin, GPIO.HIGH)
            GPIO.output(MotorPinA, GPIO.HIGH)
            GPIO.output(MotorPinB, GPIO.LOW)
            GPIO.output(YellowLedPin, GPIO.HIGH)
            GPIO.output(RedLedPin, GPIO.LOW)
            time.sleep(5)

            GPIO.output(MotorEnablePin, GPIO.LOW)
            GPIO.output(YellowLedPin, GPIO.LOW)
            time.sleep(5)

            GPIO.output(MotorEnablePin, GPIO.HIGH)
            GPIO.output(MotorPinA, GPIO.LOW)
            GPIO.output(MotorPinB, GPIO.HIGH)
            GPIO.output(YellowLedPin, GPIO.LOW)
            GPIO.output(RedLedPin, GPIO.HIGH)
            time.sleep(5)

            GPIO.output(MotorEnablePin, GPIO.LOW)
            GPIO.output(RedLedPin, GPIO.LOW)
            time.sleep(5)
    except KeyboardInterrupt:
        destroy()

def destroy():
    GPIO.output(MotorEnablePin, GPIO.LOW)
    GPIO.output(YellowLedPin, GPIO.LOW)
    GPIO.output(RedLedPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    loop()