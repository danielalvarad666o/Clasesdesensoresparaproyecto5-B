
#importaciones---------------------------------
import board
from Menu import menu
from Clases import rueda,sensoredeGas


#Instancias------------------------------------

elmenu=menu.interfasMenu()
larueda=rueda.MotorDriver()
eldegas=sensoredeGas.MQ4(26)


#variables---------------------------------------
opcion=0

#logicaaa--------------------------------------
while opcion!=2:
     opcion=elmenu.MostrarMenu()
     
     if opcion==1:
             larueda.go_left()
             ppm_value = eldegas.read_ppm()
             print("Valor de PPM: {}".format(ppm_value))
             
         