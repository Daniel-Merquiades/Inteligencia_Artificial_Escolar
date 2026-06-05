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
                "2": "apagar_luz",
                "3": "ligar_quadra",
                "4": "apagar_quadra",
                "5": "fazer_chamada",
                "6": "consultar_aluno",
                "7": "saudacao",
                "8": "encerrar"
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
        
        if intencao == "ligar_luz":
             self.falar("Ligando as luzes!")
        elif intencao == "apagar_luz":
             self.falar("Apagando as luzes!")
        elif intencao == "ligar_quadra":
            self.falar("Ligando as luzes da quadra!")
        elif intencao == "apagar_quadra":
             self.falar("Apagando as luzes da quadra!")
        elif intencao == "fazer_chamada":
             self.falar("Iniciando chamada da turma!")
        elif intencao == "saudacao":
             self.falar("Olá! Como posso ajudar?")
        elif intencao =="consultar_aluno":
             self.falar("Buscando dados sobre o aluno...")
        elif intencao == "encerrar":
             self.falar("Encerrando o sistema. Até logo!")
             raise KeyboardInterrupt
        else:
             self.falar(f"Recebi o comando mas ainda não sei executar isso. Desculpe...")
