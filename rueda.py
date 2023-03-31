import RPi.GPIO as GPIO
import time

in1 = 6   # Pin que controla el sentido de giro Motor A
in2 = 5   # Pin que controla el sentido de giro Motor A

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)   # Configura los pines como salida
GPIO.setup(in2, GPIO.OUT)



while True:
    opcion=input("Escoje una opcion: ")
    if (opcion == '1'):  # Si el comando es '1'
        GPIO.output(in1, GPIO.LOW)  # GIRO DERECHA
        GPIO.output(in2, GPIO.HIGH)
    elif (opcion == '2'):  # Si el comando es '2'
        GPIO.output(in1, GPIO.HIGH)  # GIRO IZQUIERDA
        GPIO.output(in2, GPIO.LOW)
    elif (opcion == '3'):  # Si el comando es '3'
        GPIO.output(in1, GPIO.LOW)  # PARA
        GPIO.output(in2, GPIO.LOW)


