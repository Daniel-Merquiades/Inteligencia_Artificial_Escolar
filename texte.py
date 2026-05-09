# teste_voz.py
from gtts import gTTS
from playsound import playsound
import os

def falar(texto):
    print(f"Falando: {texto}")
    tts = gTTS(text=texto, lang='pt-br', slow=False)
    tts.save("temp_audio.mp3")      # salva como mp3
    playsound("temp_audio.mp3")     # reproduz
    os.remove("temp_audio.mp3")     # apaga depois

falar("Olá, estou funcionando!")
falar("Essa é a segunda fala!")
falar("E essa é a terceira!")
print("Fim do teste!")