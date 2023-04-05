class interfasMenu:
    
    def MostrarMenu(self) -> int :
        print("")
        print("[Seleccion]"+"-----------------------"*10)
        print("1)OPCIONES DE SERIAL")
        print("2)OPCIONES DE RUEDA")
        print("3)DHT11")
        
       
        print("4)salir")
        option=int(input("Escoge una opcion: "))
        print("")
        return option