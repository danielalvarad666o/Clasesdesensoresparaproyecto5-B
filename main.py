
#importaciones---------------------------------
import board
from Menu import menu
from Clases import rueda,sensoredeGas

#Instancias------------------------------------
elmenu=menu.interfasMenu()
larueda=rueda.MotorDriver()
gas=sensoredeGas.AnalogRead(board.A4)
gas1=sensoredeGas.AnalogRead(board.A5)

#variables---------------------------------------
opcion=0

#logicaaa--------------------------------------
while opcion!=2:
     opcion=elmenu.MostrarMenu()
     
     if opcion==1:
             larueda.go_left()
             gas.read()
             gas1.read()
             
         