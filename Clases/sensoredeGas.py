import time
import RPi.GPIO as GPIO

class MQ4:
    def __init__(self, pin=0):
        self.pin = pin
        self.RL = 1  # Resistance of the load resistor in kilo ohms
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def read_raw(self):
        adc_value = GPIO.input(self.pin)
        return adc_value

    def read_rs(self):
     voltage = self.read_raw()
     if voltage == 0:
        return 0
     rs = (3.3 - voltage) / voltage * self.RL
     return rs


    def read_ppm(self):
        rs = self.read_rs()
        ppm = (rs / 9.9) ** -1.6  # Algorithm for calculating PPM
        return ppm

    def __del__(self):
        GPIO.cleanup()
