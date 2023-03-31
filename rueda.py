import RPi.GPIO as GPIO
import time

in1 = 6   # Pin que controla el sentido de giro Motor A


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)   # Configura los pines como salida

while True:
    GPIO.output(in1, GPIO.HIGH)  # Enciende el motor
    time.sleep(1)  # Espera 1 segundo
    GPIO.output(in1, GPIO.LOW)  # Apaga el motor
    time.sleep(1)  # Espera 1 segundo

GPIO.cleanup()  # Limpia los pines GPIO al salir del programa


