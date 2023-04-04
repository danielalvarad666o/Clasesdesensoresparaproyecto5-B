
#importaciones---------------------------------
from Menu import menu
from Interface import interfaceRueda,interfaceSerial




#Instancias------------------------------------
elmenu=menu.interfasMenu()





#variables---------------------------------------
opcion=0

#logicaaa--------------------------------------
while opcion!=2:
     opcion=elmenu.MostrarMenu()
     
     if opcion==1:
             elserial=interfaceSerial.interfaceSerial()
     
     elif opcion==2:
             lainterfacerueda=interfaceRueda.interfaceRueda()
             
             
            
             
         