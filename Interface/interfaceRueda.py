from Clases import rueda
larueda=rueda.MotorDriver()

class interfaceRueda: 
    def __init__(self) -> None:
        print("--"*10)
        print("1)PRENDER ALA DERECHA ")
        print("2)PRENDER ALA IZQUIERDA ")
        print("1)APAGAR ")
        opcion=int(input("Escoje Una Opcion: "))
        if opcion==1:
            larueda.go_right()
        elif opcion==2:
            larueda.go_left()
        elif opcion==3:
            larueda.stop()
        
        
   