import serial
import serial.tools.list_ports
import time

class Controles:
    def __init__(self):
        self.arduino = None
        self.conectar()

    def conectar(self):
        """
     Tenta conectar automaticamente ao Arduino.
        """
        portas = serial.tools.list_ports.comports()
        for porta in portas:
            if "Arduino" in porta.description or "CH340" in porta.description or "USB" in porta.description:
              try:
                  self.arduino=serial.Serial(porta.device, 9600, timeout=1)
                  time.sleep(2) #vai esperar o arduino inicializar
                  print(f"[ARDUINO] Conectado em {porta.device}!")
              except:
                  continue
        print("[ARDUINO]!! AVISO !! Arduino não encontrado.")
        print("[ARDUINO] Rodando em modo simulação.")
    def enviar(self,comando):
        """
      Manda um comando para o Arduino.
      Se não tiver Arduino, simula no terminal
        """
        if self.arduino and self.arduino.is_open:
            self.arduino.write(f"'{comando}'\n".encode())
            print(f"[ARDUINO] Enviado: '{comando}'")
        else:
            print(f"[SIMULAÇÂO] Comando: '{comando}'")

    # SALAS DE AULA + COORDENAÇÃO
    def ligar_sala1(self):
        self.enviar("LIGA_SALA1")
    def apagar_sala1(self):
        self.enviar("APAGA_SALA1")
    def ligar_sala2(self):
        self.enviar("LIGAR_SALA2")
    def apagar_sala2(self):
        self.enviar("APAGAR_SALA2")
    def ligar_coordenacao(self):
        self.enviar("LIGA_COORDENAÇÂO")
    def apagar_coordenacao(self):
        self.enviar("APAGA_COORDENAÇÃO")

    # Quadra 
    def ligar_quadra(self):
        self.enviar("LIGA_QUADRA")
    def apagar_quadra(self):
        self.enviar("APAGA_QUADRA")
    
    # Geral
    def ligar_tudo(self):
        self.enviar("LIGA_TUDO")
    def apagar_tudo(self):
        self.enviar("APAGA_TUDO")
    
    def fechar(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
            print("[ARDUINO] Conexão encerrada.")
            