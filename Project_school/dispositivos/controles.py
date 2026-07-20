import serial
import serial.tools.list_ports
import time

class Controles:
    def __init__(self):
        self.arduino = None
        self.conectar()

    def conectar(self):
        portas = serial.tools.list_ports.comports()
        for porta in portas:
            if "Arduino" in porta.description or "CH340" in porta.description or "USB" in porta.description:
                try:
                    self.arduino = serial.Serial(porta.device, 9600, timeout=1)
                    time.sleep(2)
                    print(f"[ARDUINO] Conectado em {porta.device}!")
                    return 
                except:
                    continue
        print("[ARDUINO] !! AVISO !! Arduino não encontrado.")
        print("[ARDUINO] Rodando em modo simulação.")

    def enviar(self, comando):
        if self.arduino and self.arduino.is_open:
            self.arduino.write(f"{comando}\n".encode())  # sem aspas extras no comando
            print(f"[ARDUINO] Enviado: '{comando}'")
        else:
            print(f"[SIMULAÇÃO] Comando: '{comando}'")

    # Salas
    def ligar_sala1(self):
        self.enviar("LIGA_SALA1")      

    def apagar_sala1(self):
        self.enviar("APAGA_SALA1")     

    def ligar_sala2(self):
        self.enviar("LIGA_SALA2")      

    def apagar_sala2(self):
        self.enviar("APAGA_SALA2")     

    def ligar_coordenacao(self):
        self.enviar("LIGA_COORD")     

    def apagar_coordenacao(self):
        self.enviar("APAGA_COORD")     

    # Quadra
    def ligar_quadra(self):
        self.enviar("LIGA_QUADRA")
