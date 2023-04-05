from Clases import DHT



class interfaceDHT:
    
    def __init__(self) -> None:
        self.sensordht=DHT.DHTSensor(21)
        
    def leertemphum(self) -> any:
        hu,=self.sensordht.read_humidity()
        temp=self.sensordht.read_temperature()
        self.valores={"Humedada: {}, Temperatura: {}".format(hu, temp)}
        return self.valores
        