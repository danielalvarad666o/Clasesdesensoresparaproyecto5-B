from Clases import seial

serialReader=seial.SerialReader()


class interfaceSerial:
    
    def __init__(self) -> None:
        serialReader.select_port()
        
    def leer(self)-> str:
       return serialReader.read()
        
    
    

        

        
