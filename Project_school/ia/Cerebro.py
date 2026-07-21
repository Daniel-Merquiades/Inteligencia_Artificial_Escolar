import speech_recognition as sr
import io
import sounddevice as sd 
import numpy as np
import io
import os
import wave 
import pickle
from gtts import gTTS
from playsound import playsound
from ia.aprendizado import Aprendizado
from dados.banco import Banco
from dispositivos.controles import Controles

class Cerebro:
    """""
    Classe principal da IA
    Por Enquanto faz o básico e tals
    mas nas proximas vai ficar do balacobaco
    """""
    def __init__(self):
        """""
        __init__ roda automaticamente quando se faz o Cerebro()
        é o momento que a ia acorda
        """""
        print("[IA] Núcleo inicializado.")
        self.controles = Controles()
        self.banco = Banco()
        self.nome= "alexa escolar"
        self.reconhecedor = sr.Recognizer()
        self.reconhecedor.energy_threshold = 300
        self.taxa_amostragem = 16000
        self.duracao_escuta = 5
        self.modelo = self.carregar_modelo()
        self.aprendizado = Aprendizado()
    
    def carregar_modelo(self):
         """""
         Carrega o modelo salvo pelo treinamento.py em formato.pkl.
         Se não encontrar, avisa o usuario e retorna None.
         """
         pasta_atual = os.path.dirname(os.path.abspath(__file__))
         caminho = os.path.join(pasta_atual, "modelo.pkl")
         if os.path.exists(caminho):
                with open(caminho, "rb") as arquivo:
                   modelo= pickle.load(arquivo)
                print(f"Modelo salvo em: '{caminho}")
                print("[IA] Modelo carregado com sucesso!")
                return modelo
         else:
              print("[IA] !! AVISO !! Modelo não encontrado.\nRode ia/treinamento.py primeiro")
              return None
              

    def falar(self, texto):
        """""
        Por enquanto so imprime
        mas futuramente falará
        """""
        print(f"[{self.nome}]: {texto}")
        tts = gTTS(text =  texto, lang="pt-br", slow= False)
        tts.save("Temp_audio.mp3")
        playsound("Temp_audio.mp3")
        os.remove("Temp_audio.mp3")
    def ouviu(self):
        """""
        depois vai receber mic
        """""
        print("\n'[IA] Escutando...")
        try:
            audio_gravado = sd.rec(
                int(self.duracao_escuta * self.taxa_amostragem),
                samplerate = self.taxa_amostragem,
                channels=1,
                dtype='int16'
            )
            sd.wait()
            print("'[IA]' Analisando... '")
            buffer = io.BytesIO()
            with wave.open(buffer, "wb") as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(self.taxa_amostragem)
                wav_file.writeframes(audio_gravado.tobytes())
            buffer.seek(0)
            with sr.AudioFile(buffer) as fonte:
                audio = self.reconhecedor.record(fonte)
                texto = self.reconhecedor.recognize_google(
                    audio,
                    language='pt-br'
                )
            print(f"Você disse:'{texto}'")
            return texto.lower()
        except sr.WaitTimeoutError:
                print("'[IA]'Aparentemente não consegui detectar nenhum som, tente novamente por favor!")
                return None
        except sr.UnknownValueError:
                self.falar("Não entendi. Poderia por gentileza repetir ?")
                return None
        except sr.RequestError:
                self.falar("No momento estou sem conexão para processar sua voz, tente novamente mais tarde.")
                return None
   
    def identificar_intencao(self, comando):
         """""
         Usa o modelo treinado para identificar a intenção do comando.
         Retorna intenção e confiança (0 a 100%)
         """""
         if self.modelo is None:
              return None, 0
         intencao = self.modelo.predict([comando])[0]
         confianca = max(self.modelo.predict_proba([comando])[0]*100)
         print(f"[IA] Intenção: '{intencao}' ('{confianca}'% de confiança)")
         return intencao, confianca
    
    def processar(self, comando):
        """""
        Recebe o comando e decide o que fazer
        """""
        intencao, confianca = self.identificar_intencao(comando)
        if confianca < 30:
             self.falar("Não tenho certeza do que você quis dizer. Pode repetir?")
             opcoes= {
                "1": "ligar_luz",
                "2": "ligar_sala1",
                "3": "ligar_sala2",
                "4": "ligar_coordenacao",
                "5": "apagar_luz",
                "6": "apagar_sala1",
                "7": "apagar_sala2",
                "8": "apagar_coordenacao",
                "9": "ligar_quadra",
                "10": "apagar_quadra",
                "11": "fazer_chamada",
                "12": "consultar_aluno",
                "13": "saudacao",
                "14": "encerrar"
             }
             print("\nOpções:")
             for num, nome in opcoes.items():
                  print(f" '{num}' -> '{nome}'")
             print("0 -> Ignorar")
             escolha = input("digite o número ").strip()
             if escolha in opcoes:
                 intencao_correta = opcoes[escolha]
                 self.aprendizado.salvar_exemplo(comando,intencao_correta)
                 self.modelo = self.aprendizado.retreinar()
                 self.falar("Entendido! Já aprendi isso")
                 intencao = intencao_correta
             else:
                 return
             
        #Ligar luzes
        if intencao == "ligar_luz":
             self.falar("Ligando as luzes!")
             self.controles.ligar_sala1()
             self.controles.ligar_sala2()
             self.controles.ligar_coordenacao()
        elif intencao =="ligar_sala1":
             self.falar("Ligando as luzes da sala 1!")
             self.controles.ligar_sala1()
        elif intencao == "ligar_sala2":
             self.falar("Ligando as luzes da sala 2!")
             self.controles.ligar_sala2()
        elif intencao == "ligar_coordenacao":
             self.falar("Ligando as luzes da coordenação!")
             self.controles.ligar_coordenacao()
        elif intencao == "ligar_patio":
             self.falar("ligando as luzes do pátio")
             self.controles.ligar_patio()

          #Apagar as luzes
        elif intencao == "apagar_luz":
             self.falar("Apagando as luzes!")
             self.controles.apagar_sala1()
             self.controles.apagar_sala2()
             self.controles.apagar_coordenacao()

        elif intencao =="apagar_sala1":
             self.falar("Apagando as luzes da sala 1!")
             self.controles.apagar_sala1()
        elif intencao == "apagar_sala2":
             self.falar("Apagando as luzes da sala 2!")
             self.controles.apagar_sala2()
        elif intencao == "apagar_coordenacao":
             self.falar("Apagando as luzes da coordenação!")
             self.controles.apagar_coordenacao()
        elif intencao == "apaga_patio":
             self.falar("Apagando as luzes do pátio")
             self.controles.apaga_patio()

          #Ligar as luzes da quadra
        elif intencao == "ligar_quadra":
            self.falar("Ligando as luzes da quadra!")
            self.controles.ligar_quadra()
          #Apagar as luzes da quadra
        elif intencao == "apagar_quadra":
             self.falar("Apagando as luzes da quadra!")
             self.controles.apaga_quadra()

          #Abrir portão principal e coordenação
        elif intencao == "abrir_portao":
             self.falar("abrindo portão de entrada!")
             self.controles.abrir_portao()
        elif intencao == "abrir_coord":
             self.falar("abrindo a porta da coordenação!")
             self.controles.abrir_coord()
          #Fechar portão principal e coordenação
        elif intencao == "fechar_portao":
             self.falar("fechando portão de entrada!")
             self.controles.fechar_portao()
        elif intencao == "fechar_coord":
             self.falar("fechando a porta da coordenação!")
             self.controles.fechar_coord()

          #Fazer a chamada
        elif intencao == "fazer_chamada":
             self.falar("Qual é a turma?")
             turma = self.ouvir_resposta()
             if not turma:
                  self.falar("Não entendi a turma, Pode repetir?")
                  return
             turma = turma.upper()
             alunos = self.banco.listar_turma(turma)

             if not alunos:
                  self.falar(f"Nenhum aluno encontrado na turma '{turma}'.")
             else:   
               self.falar("Iniciando chamada da turma '{turma}'!")
               for aluno in alunos:
                    self.falar(f"{aluno[1]}.")
                    resposta = self.ouvir_resposta()
                    if resposta and ("sim" in resposta.lower() or "presente" in resposta.lower() or "aqui" in resposta.lower()):
                         presente = 1
                    else :
                         presente = 0
                    self.banco.registrar_chamada(aluno[0], presente)
               self.falar("Chamada Finalizada! O que mais posso fazer por você?")

          #Saudações
        elif intencao == "saudacao":
             self.falar("Olá! Como posso ajudar?")

          #Consultar o aluno
        elif intencao =="consultar_aluno":
             while True:
                     self.falar("Qual é o nome do aluno?")
                     nome = self.ouvir_resposta()
                     if not nome:
                          continue
                     resultados = self.banco.buscar_aluno(nome)

                     if resultados:
                          for aluno in resultados:
                               self.falar(f"Aluno encontrado: {aluno[1]}, turma {aluno[2]}, {aluno[3]} anos.")
                          self.falar("Deseja consultar outro aluno?")
                          resposta = self.ouvir_resposta()
                          if resposta and "sim"in resposta.lower():
                               continue
                          else:
                             break
                     else:
                          self.falar(f"Nenhum aluno encontrado com o nome: {nome}. Deseja tentar novamente?")
                          resposta= self.ouvir_resposta()
                     if resposta and "sim" in resposta.lower():
                          continue
                     else:
                          self.falar("OK, o que mais posso fazer por você?")
                          break
                  

          #Encerramento do sistema
        elif intencao == "encerrar":
             self.falar("Encerrando o sistema. Até logo!")
             raise KeyboardInterrupt
        else:
             self.falar(f"Recebi o comando mas ainda não sei executar isso. Desculpe...")

    def ouvir_resposta(self):
         """
         Ouve uma resposta curta do usuário.
         Usado para captar nome de alundo, turma e etc.
         """
         print("\n[IA] Ouvindo resposta...")
         try:
              audio_gravado =sd.rec(
                   int(self.duracao_escuta * self.taxa_amostragem), samplerate=self.taxa_amostragem,
                   channels = 1,
                   dtype= 'int16'
              )
              sd.wait()
              buffer = io.BytesIO()
              with wave.open(buffer, "wb") as wav_file:
                   wav_file.setnchannels(1)
                   wav_file.setsampwidth(2)
                   wav_file.setframerate(self.taxa_amostragem)
                   wav_file.writeframes(audio_gravado.tobytes())
                   buffer.seek(0)
                   with sr.AudioFile(buffer) as fonte:
                        audio = self.reconhecedor.record(fonte)

                   texto = self.reconhecedor.recognize_google(audio, language="pt-BR")
                   print(f"[IA] Ouviu: '{texto}' ")
                   return texto.strip()
         except sr.UnknownValueError:
              self.falar("Não entendi. Pode repetir?")
              return None
         except Exception as e:
              print(f"[ERRO] {e}")
              return None