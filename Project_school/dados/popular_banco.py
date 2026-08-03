# Roda esse arquivo UMA vez para popular o banco com alunos de exemplo
from banco import Banco
banco = Banco()

# Turma 3°ANO
banco.adicionar_aluno("Josefina de Jesus", "3°", 17)
banco.adicionar_aluno("Raiane Santana", "3°", 17)
banco.adicionar_aluno("Cleiton dos Santos", "3°", 18)
banco.adicionar_aluno("Fernando Pessoa", "3°", 18)
banco.adicionar_aluno("Roberta francisca", "3°", 18)

#turma 2°ANO
banco.adicionar_aluno("Gustavo Marques", "2°", 16)
banco.adicionar_aluno("Gabrielly dos Santos", "2°", 17)
banco.adicionar_aluno("Pedro Costa", "2°", 16)
banco.adicionar_aluno("Maria Eduarda", "2°", 17)
banco.adicionar_aluno("Mariana de Jesus", "2°", 16)

banco.fechar()
print("\nBanco populado com sucesso!")