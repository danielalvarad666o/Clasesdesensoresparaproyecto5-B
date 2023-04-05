
#importaciones---------------------------------
from Menu import menu
from Interface import interfaceRueda,interfaceSerial,interfacertemperatura




#Instancias------------------------------------
elmenu=menu.interfasMenu()
dht11=interfacertemperatura.interfaceDHT()





#variables---------------------------------------
opcion=0

#logicaaa--------------------------------------
while opcion!=2:
     opcion=elmenu.MostrarMenu()
     
     if opcion==1:
             elserial=interfaceSerial.interfaceSerial()
     
     elif opcion==2:
             lainterfacerueda=interfaceRueda.interfaceRueda()
     elif opcion==3:
             dht11.leertemphum()
             
             
             
             
            
             
         