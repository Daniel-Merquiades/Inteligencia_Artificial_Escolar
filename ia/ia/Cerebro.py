class Cerebro:
    """""
    Classe principal da IA
    Por Enquanto faz o básico e tals
    mas nas proximas vai ficar do balacobaco
    """""
    def __init__(self):
        """""
        __init__ roda auto quando se faz o Cerebro()
        é comoo momento que a ia acorda
        """""
        print("[IA] Núcleo inicializado.")
        self.nome= "alexa escolar"
    def falar(self, texto):
        """""
        Por enqunto so imprime
        mas futuramente falará
        """""
        print(f"[{self.nome}]: {texto}")
    def ouviu(self):
        """""
        depois vai receber mic
        """""
        entrada= input("Você: ").strip().lower()
        return entrada if entrada else None
    def processar(self, comando):
        """""
        Recebe o comando e decide o que fazer
        """""
        if comando == "sair":
            raise KeyboardInterrupt
        self.falar(f"Recebi o comando: '{comando}'. Em breve saberei o que fazer!")