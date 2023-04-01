import RPi.GPIO as GPIO
import time

# Define los pines que controlan el puente H
in1 = 5
in2 = 6

# Configura la Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

while True:
    comando = input("Ingresa un comando (1, 2 o 3): ")
    
    if comando == '1':  # Si el comando es '1'
        GPIO.output(in1, GPIO.LOW)  # Giro hacia la derecha
        GPIO.output(in2, GPIO.HIGH)
    elif comando == '2':  # Si el comando es '2'
        GPIO.output(in1, GPIO.HIGH)  # Giro hacia la izquierda
        GPIO.output(in2, GPIO.LOW)
    elif comando == '3':  # Si el comando es '3'
        GPIO.output(in1, GPIO.LOW)  # Para el motor
        GPIO.output(in2, GPIO.LOW)
        
    time.sleep(0.1)  # Pequeña pausa para evitar la sobrecarga del procesador



