import RPi.GPIO as GPIO
import time
from dht11 import DHT11

class DHTSensor:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin
        self.dht11 = DHT11(pin)

    def read_temperature(self):
        result = self.dht11.read()
        if result.is_valid():
            return result.temperature
        else:
            return None

    def read_humidity(self):
        result = self.dht11.read()
        if result.is_valid():
            return result.humidity
        else:
            return None

# if __name__ == '__main__':
#     sensor = DHTSensor(20)

#     for i in range(5):
#         temperature = sensor.read_temperature()
#         humidity = sensor.read_humidity()
#         if temperature is not None and humidity is not None:
#             print('Temperature: {0} C, Humidity: {1} %'.format(temperature, humidity))
#         else:
#             print('Failed to read data from DHT11 sensor.')

#         time.sleep(2)

   # GPIO.cleanup()
