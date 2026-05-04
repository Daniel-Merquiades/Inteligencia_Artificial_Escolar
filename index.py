from ia.cerebro import Cerebro
def main():
    print("-=-"*40)
    print("INTELIGÊNCIA ESCOLAR -- INICIANDO SISTEMA...")
    print("-=-"*40)
#ia = Cerebro()
ia.falar= ("Sistema inicializado. Como posso ajudar? ")
while True:
    try:
        comando= ia.ouvir()
        if comando:
            ia.processar(comando)
    except KeyboardInterrupt
    ia.falar("Encerrando sistema. Até breve")
    break
if __main__ == "__main__":
    main()