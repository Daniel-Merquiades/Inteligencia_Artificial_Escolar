import speech_recognition as sr
import io
import sounddevice as sd 
import numpy as np
import io
import os
import wave 
from gtts import gTTS
from playsound import playsound

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

    def falar(self, texto):
        """""
        Por enqunto so imprime
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
        
    def processar(self, comando):
        """""
        Recebe o comando e decide o que fazer
        """""
        if comando == "sair":
            raise KeyboardInterrupt
        if "sair" in comando or "encerrar" in comando:
            raise KeyboardInterrupt
        elif "olá" in comando or "oi" in comando:
            self.falar("Olá! Prazer em conhecer. Como posso ajudar?")
        elif "seu nome" in comando or "quem é você" in comando:
            self.falar("Eu sou a Inteligência Artificial Escolar. Estou aqui para te ajudar no controle da sua escola!")
        else:
            self.falar(f"Recebi o comando '{comando}'. Em breve saberei o que fazer!")