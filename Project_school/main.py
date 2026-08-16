import __main__
from ia.Cerebro import Cerebro
import sys
def main():
    modo_site = '--site' in sys.argv
    print("-=-"*40)
    print("INTELIGÊNCIA ESCOLAR -- INICIANDO SISTEMA...")
    print("-=-"*40)
    ia = Cerebro(modo_site=modo_site)
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