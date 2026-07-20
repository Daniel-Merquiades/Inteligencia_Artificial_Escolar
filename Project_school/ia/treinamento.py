from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
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

    # Ligar sala 1

    ("liga a sala 1", "ligar_sala1"),
    ("liga a sala um", "ligar_sala1"),
    ("acende a sala 1", "ligar_sala1"),
    ("acende a sala um", "ligar_sala1"),
    ("ligar sala 1", "ligar_sala1"),
    ("ligar sala um", "ligar_sala1"),
    ("luz da sala 1", "ligar_sala1"),
    ("luz da sala um", "ligar_sala1"),
    ("ilumina a sala 1", "ligar_sala1"),
    ("ilumina a sala um", "ligar_sala1"),
    ("ligar as luzes da sala 1", "ligar_sala1"),
    ("ligar as luzes da sala um", "ligar_sala1"),
    ("acender as luzes da sala 1", "ligar_sala1"),
    ("quero luz na sala 1", "ligar_sala1"),
    ("quero luz na sala um", "ligar_sala1"),

    # Apagar sala 1

    ("apaga a sala 1", "apagar_sala1"),
    ("apaga a sala um", "apagar_sala1"),
    ("desliga a sala 1", "apagar_sala1"),
    ("desliga a sala um", "apagar_sala1"),
    ("apagar sala 1", "apagar_sala1"),
    ("apagar sala um", "apagar_sala1"),
    ("desligar sala 1", "apagar_sala1"),
    ("desligar sala um", "apagar_sala1"),
    ("apagar as luzes da sala 1", "apagar_sala1"),
    ("apagar as luzes da sala um", "apagar_sala1"),
    ("desligar as luzes da sala 1", "apagar_sala1"),
    ("sem luz na sala 1", "apagar_sala1"),

    # Ligar sala 2

    ("liga a sala 2", "ligar_sala2"),
    ("liga a sala dois", "ligar_sala2"),
    ("acende a sala 2", "ligar_sala2"),
    ("acende a sala dois", "ligar_sala2"),
    ("ligar sala 2", "ligar_sala2"),
    ("ligar sala dois", "ligar_sala2"),
    ("luz da sala 2", "ligar_sala2"),
    ("luz da sala dois", "ligar_sala2"),
    ("ilumina a sala 2", "ligar_sala2"),
    ("ilumina a sala dois", "ligar_sala2"),
    ("ligar as luzes da sala 2", "ligar_sala2"),
    ("ligar as luzes da sala dois", "ligar_sala2"),
    ("acender as luzes da sala 2", "ligar_sala2"),
    ("quero luz na sala 2", "ligar_sala2"),
    ("quero luz na sala dois", "ligar_sala2"),

    # Apagar sala 2

    ("apaga a sala 2", "apagar_sala2"),
    ("apaga a sala dois", "apagar_sala2"),
    ("desliga a sala 2", "apagar_sala2"),
    ("desliga a sala dois", "apagar_sala2"),
    ("apagar sala 2", "apagar_sala2"),
    ("apagar sala dois", "apagar_sala2"),
    ("desligar sala 2", "apagar_sala2"),
    ("desligar sala dois", "apagar_sala2"),
    ("apagar as luzes da sala 2", "apagar_sala2"),
    ("apagar as luzes da sala dois", "apagar_sala2"),
    ("desligar as luzes da sala 2", "apagar_sala2"),
    ("sem luz na sala 2", "apagar_sala2"),

    # Ligar coordenação

    ("liga a coordenação", "ligar_coordenacao"),
    ("ligar coordenação", "ligar_coordenacao"),
    ("acende a coordenação", "ligar_coordenacao"),
    ("acender coordenação", "ligar_coordenacao"),
    ("luz da coordenação", "ligar_coordenacao"),
    ("ilumina a coordenação", "ligar_coordenacao"),
    ("ligar as luzes da coordenação", "ligar_coordenacao"),
    ("acender as luzes da coordenação", "ligar_coordenacao"),
    ("quero luz na coordenação", "ligar_coordenacao"),
    ("coordenação luz", "ligar_coordenacao"),

    # Apagar coordenação

    ("apaga a coordenação", "apagar_coordenacao"),
    ("apagar coordenação", "apagar_coordenacao"),
    ("desliga a coordenação", "apagar_coordenacao"),
    ("desligar coordenação", "apagar_coordenacao"),
    ("apagar as luzes da coordenação", "apagar_coordenacao"),
    ("desligar as luzes da coordenação", "apagar_coordenacao"),
    ("sem luz na coordenação", "apagar_coordenacao"),

    #Comandos para desligar as luzes

    ("apague as luzes", "apagar_luz"),
    ("desligue as luzes","apagar_luz"),
    ("encerre as luzes", "apagar_luz"),
    ("apagar luz", "apagar_luz"),
    ("desligar luz", "apagar_luz"),
    ("sem luz", "apagar_luz"),

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
    ("tfidf", TfidfVectorizer( ngram_range=(1, 3), analyzer = "char_wb")),
    ("classificador", SVC(kernel="linear",probability=True,C=10))
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

print(f"Modelo salvo em: '{caminho_modelo}'")
    