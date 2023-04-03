import time
import board
import analogio

class AnalogRead:
    def __init__(self, pin):
        self.pin = analogio.AnalogIn(pin)
    
    def read(self):
        return self.pin.value
    
    def __del__(self):
        self.pin.deinit()