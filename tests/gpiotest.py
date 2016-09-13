#I wrote this code to test the pins on the GPIO board I'll be using
#for the sprinkler station
import RPi.GPIO as GPIO
import time
now = time.time()
l = [27,22,13,19,26,12,16,20] #These are the BCM GPIO pin numbers
iter = 25 #number of iterations for the loop
sec = .05 #Number of seconds each LED will be on
estime = iter*8*sec
print "Estimated runtime: ", estime, " secs"
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for y in l:
 GPIO.setup(y, GPIO.OUT)
 GPIO.output(y, GPIO.LOW)
for x in range(iter):
 for y in l:
  GPIO.output(y, GPIO.HIGH)
  time.sleep(sec)
  GPIO.output(y, GPIO.LOW)
GPIO.cleanup()
done = time.time()
print "Calculated runtime: ", round(done - now,1), " secs"
