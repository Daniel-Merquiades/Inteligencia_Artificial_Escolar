# Roda esse arquivo UMA vez para popular o banco com alunos de exemplo
from dados.banco import Banco
banco = Banco()

# Turma 9A
banco.adicionar_aluno("Josefina de Jesus", "9A", 14)
banco.adicionar_aluno("Raiane Santana", "9A", 14)
banco.adicionar_aluno("Cleiton dos Santos", "9A", 15)
banco.adicionar_aluno("Fernando Pessoa", "9A", 15)
banco.adicionar_aluno("Roberta francisca", "9A", 14)

#turma 8B
banco.adicionar_aluno("Gustavo Marques", "8B", 13)
banco.adicionar_aluno("Gabrielly dos Santos", "8B", 14)
banco.adicionar_aluno("Pedro Costa", "8B", 13)
banco.adicionar_aluno("Maria Eduarda", "8B", 13)
banco.adicionar_aluno("Mariana de Jesus", "8B", 14)

banco.fechar()
print("\nBanco populado com sucesso!")