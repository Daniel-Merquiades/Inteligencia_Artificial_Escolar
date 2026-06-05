import __main__
from ia.Cerebro import Cerebro
def main():
    print("-=-"*40)
    print("INTELIGÊNCIA ESCOLAR -- INICIANDO SISTEMA...")
    print("-=-"*40)
    ia = Cerebro()
    ia.falar("Sistema inicializado. Como posso ajudar? ")
    while True:
        try:
            comando= ia.ouviu()
            if comando:
                ia.processar(comando)
        except KeyboardInterrupt:

            break
if __name__ == "__main__":
    main()