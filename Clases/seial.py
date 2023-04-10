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
     ports = serial.tools.list_ports.comports()
     print("Puertos COM disponibles:")
     for port in ports:
        print(port.device)
    
     selected_port = None
     while not selected_port:
        try:
            selection = input("Selecciona un puerto COM: ")
            if selection in [port.device for port in ports]:
                selected_port = selection
                self.ser = serial.Serial(selected_port, 9600)
                print(f"Puerto {selected_port} seleccionado.")
            else:
                print("Selección inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")
