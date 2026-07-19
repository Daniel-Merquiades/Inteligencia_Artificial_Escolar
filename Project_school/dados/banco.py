import sqlite3
import os

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
        self.cursor.execute(""" SELECT * FROM alunos WHERE turma = ? ORDER BY nome""", (turma,))
        return self.cursor.fetchall() 
    
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