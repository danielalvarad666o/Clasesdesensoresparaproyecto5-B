import RPi.GPIO as GPIO
import time

in1 = 4  # Pin que controla el sentido de giro Motor A
in2 = 5  # Pin que controla el sentido de giro Motor A

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)  # Configura los pines como salida
GPIO.setup(in2, GPIO.OUT)

print("Escoje una opcion")

while True:
    comando = input("Escoje una opcion: ")  # Lee el comando entrante
    if comando == '1':  # Si el comando es '1'
        GPIO.output(in1, GPIO.LOW)  # GIRO DERECHA
        GPIO.output(in2, GPIO.HIGH)
    elif comando == '2':  # Si el comando es '2'
        GPIO.output(in1, GPIO.HIGH)  # GIRO IZQUIERDA
        GPIO.output(in2, GPIO.LOW)
    elif comando == '3':  # Si el comando es '3'
        GPIO.output(in1, GPIO.LOW)  # PARA
        GPIO.output(in2, GPIO.LOW)
    else:
        print("Comando no válido")
    
    time.sleep(0.1)  # Pequeña pausa para evitar la sobrecarga del puerto serial

