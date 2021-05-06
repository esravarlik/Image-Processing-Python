import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

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