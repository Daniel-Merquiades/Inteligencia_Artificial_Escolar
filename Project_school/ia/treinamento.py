from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# NÃO RODE ESSE CÓDIGO! CASO FAÇA ISSO A IA IRÁ RESETAR, JOGANDO TODO APRENDIZADO DELA NO LIXO. Caso não tenha ensinado nada a ela, pode rodar de boa.

Dados = [
    #Comandos para ligar luzes

    ("liga a luz", "ligar_luz"),
    ("ligar luzes", "ligar_luz"),
    ("ascender luzes","ligar_luz"),
    ("iluminar sala", "ligar_luz"),
    ("ascede as luzes", "ligar_luz"),
    ("ligar iluminação", "ligar_luz"),
    ("luz ligar", "ligar_luz"),
    ("quero luz", "ligar_luz"),
    ("iniciar luzes","ligar_luz"),

    #Comandos para desligar as luzes

    ("apague as luzes", "apagar_luzes"),
    ("desligue as luzes","apagar_luzes"),
    ("encerre as luzes", "apagar_luzes"),
    ("apagar luz", "apagar_luzes"),
    ("desligar luz", "apagar_luzes"),
    ("sem luz", "apagar_luzes"),

    #Comandos para ligar luzes da quadra

    ("ligar luzes da quadra", "ligar_quadra"),
    ("ligar quadra", "ligar_quadra"),
    ("luzes quadra","ligar_quadra"),
    ("ascenda luzes da quadra", "ligar_quadra"), 
    ("ascender quadra", "ligar_quadra"),
    ("ligar quadra" , "ligar_quadra"),

    #Comandos para desligar as luzes da quadra
    ("desliga tudo na quadra", "apagar_quadra"),
    ("apagar quadra", "apagar_quadra"),
    ("apagar luzes da quadra", "apagar_quadra"),
    ("encerrar quadra", "apagar_quadra"),
    ("desligar quadra", "apagar_quadra"),
    ("desligar iluminação da quadra", "apagar_quadra"),

    #Comando para a realizar chamada

    ("realize a chamada", "fazer_chamada"),
    ("realizar chamada", "fazer_chamada"),
    ("fazer chamada","fazer_chamada"),
    ("registrar presença", "fazer_chamada"),
    ("iniciar chamada", "fazer_chamada"),

    #Comandos para consultar o aluno (série,presença,boletim e etc)

    ("consulta o aluno","consultar_aluno"),
    ("consulte o aluno", "consultar_aluno"),
    ("busque o aluno", "consultar_aluno"),
    ("informações sobre o aluno", "consultar_aluno"),
    ("busque o estudante", "consultar_aluno"),
    ("informações sobre o estudante", "consultar_aluno"),
    ("dados do aluno", "consultar_aluno"),
    ("dados do estudante", "consultar_aluno"),
    ("pesquise aluno", "consultar_aluno"),
    ("pesquise estudante","consultar_aluno"),

    #Saudação

    ("oi tudo bem", "saudacao"),
    ("olá", "saudacao"),
    ("oi", "saudacao"),
    ("tudo bem", "saudacao"),
    ("Ola ia","saudacao"),
    ("saudação", "saudacao"),
    ("eai", "saudacao"),
    ("fala fi", "saudacao"),
    ("tudo certo", "saudacao"),

    #Encerramento

    ("sair", "encerrar"),
    ("encerrar","encerrar"),
    ("fechar sistema","encerrar"),
    ("desligar","encerrar"),
    ("desligar sistema","encerrar")
]

frases = [item[0] for item in Dados]
intencoes = [item[1] for item in Dados]
modelo = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classificador", LogisticRegression())
])
print("Treinando a IA Escolar...")
modelo.fit(frases,intencoes)

testes = [
    "acende a luz por favor",
    "quero fazer a chamada agora",
    "me dá informações sobre o aluno João",
    "desliga tudo na quadra",
    "oi tudo bem",
]

print("\nTestando o modelo:")
print("-"*40)
for frases in testes:
    intencao = modelo.predict([frases])[0]
    print(f"'{frases}' -> '{intencao}'")

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_modelo = os.path.join(pasta_atual, "modelo.pkl")
with open(caminho_modelo, "wb") as arquivo:
    pickle.dump(modelo, arquivo)
print("-"*40)
if __name__ == "__main__":
    modelo.fit(frases, intencoes)
    with open(caminho_modelo, "wb") as arquivo:
        pickle.dump(modelo, arquivo)
    print(f"Modelo salvo em: '{caminho_modelo}'")
    