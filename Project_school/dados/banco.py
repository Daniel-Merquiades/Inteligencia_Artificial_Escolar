import sqlite3
import os
import re

NUMEROS_EXTENSO = {
    "primeiro": "1",
    "segundo": "2",
    "terceiro": "3",
    "quarto": "4",
    "quinto": "5",
    "sexto": "6",
    "setimo": "7",
    "sétimo": "7",
    "oitavo": "8",
    "nono": "9",
    "nuno": "9",
    "decimo": "10",
    "décimo": "10",
}

def normalizar_turma(texto):
    """
    Deixa o texto de uma turma em um formato padrão independente de como foi falado ou digitado. Como por exemplo:
    9°A ---- 9a
    nono a ---- 9a
    oitavob ---- 8b
    8 B ---- 8b
    """

    texto= texto.lower().strip()
    texto = texto.replace("°","").replace("º","").replace(".","").replace("-","")

    for extenso, digito in NUMEROS_EXTENSO.items():
        texto = re.sub(rf"\b{extenso}\b", digito, texto)
    texto = texto.replace(" ","")
    return texto

class Banco:
    def __init__(self):
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(pasta_atual, "escola.db")
        self.conexao = sqlite3.connect(caminho)
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()
        print("[BANCO] Banco de dados inicializado com sucesso!")
    def criar_tabelas(self):

        """
        Cria as tabelas caso ainda não existam.
        """
        #tabelas de alunos
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, turma TEXT NOT NULL, idade INTEGER) """)

        #tabela de chamadas
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS chamadas (id  INTEGER PRIMARY KEY AUTOINCREMENT, aluno_id INTEGER NOT NULL, data TEXT NOT NULL, presente INTEGER NOT NULL, FOREIGN KEY (aluno_id) REFERENCES alunos(id) ) """)

        self.conexao.commit()
    
    def adicionar_aluno(self,nome,turma,idade):
        """"
        Cadastra um novo aluno no banco de dados.
        """
        self.cursor.execute(""" INSERT INTO alunos(nome, turma, idade) VALUES(?, ?, ?) """, (nome,turma,idade))
        self.conexao.commit()
        print(f"[BANCO] Aluno '{nome}' cadastrado!")
    
    def buscar_aluno(self,nome):
        """
        Busca um aluno pelo nome.
        """
        self.cursor.execute("""  SELECT * FROM alunos WHERE nome LIKE ? OR nome = ? """, (f"%{nome}%", nome))
        return self.cursor.fetchall()
    
    def listar_turma(self, turma):
        """
        Lista todos os alunos de uma turma
        """
        turma_normalizada = normalizar_turma(turma) ## erro está aqui, o valor nao está sendo associado, com isso o terminal não consegue utilizar a variável
        self.cursor.execute("SELECT * FROM alunos")
        todos_alunos = self.cursor.fetchall()

        resultado = [
            aluno for aluno in todos_alunos
            if normalizar_turma(aluno[2]) == turma_normalizada
        ]
        
        resultado.sort(key=lambda aluno: aluno[1])
        return resultado
    
    def registrar_chamada(self, aluno_id, presente):
        """
        Registra presença ou falta de um aluno.
        Presente = 1 (presente) ou 0 (faltou)
        """
        from datetime import date
        hoje = date.today().strftime("%Y-%m-%d")
        self.cursor.execute(""" INSERT INTO chamadas (aluno_id, data, presente) VALUES (?, ?, ?) """, (aluno_id, hoje, presente))
        self.conexao.commit()

    def ver_chamada(self, turma):
        """
        Mostra a chamada de hoje de uma turma
        """
        from datetime import date
        hoje = date.today().strftime("%Y-%m-%d")
        self.cursor.execute(""" SELECT alunos.nome, chamadas.presente FROM chamadas JOIN alunos ON chamadas.aluno_id = alunos.id WHERE alunos.turma = ? AND chamadas.data = ? ORDER BY alunos.nome""", (turma, hoje))
        return self.cursor.fetchall()
    
    def fechar(self):
        self.conexao.close()