import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
time.sleep(5)
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.cleanup()
