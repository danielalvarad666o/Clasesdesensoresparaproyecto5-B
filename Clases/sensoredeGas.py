import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class AnalogRead:
    def __init__(self, pin):
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        self.pin = AnalogIn(ads, pin)

    def read(self):
        VALOR = self.pin.value
        print(VALOR)
        time.sleep(0.5)
    
    def __del__(self):
        self.pin.deinit()
