import serial.tools.list_ports

class SerialReader:
    def __init__(self):
        self.ser = None
    
    def read(self):
        if self.ser:
            return self.ser.readline().decode().strip()
        else:
            print("No se ha seleccionado un puerto COM.")
    
    def select_port(self):
     portList=[]
     ports = serial.tools.list_ports.comports()
     print("Puertos disponibles:")
     for i, port in enumerate(ports):
        portList.append(port.device)
        print(f"{i+1}. {port.device}")
    
     selected_port = None
     while not selected_port:
        try:
            selection = int(input("Selecciona un puerto: "))
            if selection > 0 and selection <= len(ports):
                selected_port = ports[selection-1].device
                self.ser = serial.Serial(selected_port, 9600)
                print(f"Puerto {selected_port} seleccionado.")
            else:
                print("Selección inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")

