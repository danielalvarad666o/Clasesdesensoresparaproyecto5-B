from Clases import DHT



class interfaceDHT:
    
    def __init__(self) -> None:
        self.sensordht=DHT.DHTSensor(21)
        
        
        
    def leertemphum(self) -> any:
       for i in range(5):
         hu=self.sensordht.read_humidity()
         temp=self.sensordht.read_temperature()
         
         print(format("Humedad"+str(hu),"Temperatura"+str(temp)))
        