import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

#Duty Cycle  
#(0,5/ 20) *100 = % 2.5 duty (0 degree)
#(1,5/ 20) *100 = % 7.5 duty (90 degree)
#(2,5/ 20) *100 = % 12.5 duty (180 degree)
#(1/ 20) *100 = % 5 duty (45 degree)
#(2/20)* 100 = %10 duty (135 degree)
#Pwm equivalent according to angle:
#Duty = (Angle/18) + 2,5

pw = GPIO.PWM(servoPIN, 50)
pw.start(2.5)
try:
  while True:
    pw.ChangeDutyCycle(5)
    time.sleep(0.5)
    pw.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    pw.ChangeDutyCycle(10)
    time.sleep(0.5)
    pw.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    pw.ChangeDutyCycle(10)
    time.sleep(0.5)
    pw.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    pw.ChangeDutyCycle(5)
    time.sleep(0.5)
    pw.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  pw.stop()
  GPIO.cleanup
