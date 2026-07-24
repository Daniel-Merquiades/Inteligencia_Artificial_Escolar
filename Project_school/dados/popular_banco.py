# Roda esse arquivo UMA vez para popular o banco com alunos de exemplo
from banco import Banco
banco = Banco()

# Turma 9°A
banco.adicionar_aluno("Josefina de Jesus", "9°A", 14)
banco.adicionar_aluno("Raiane Santana", "9°A", 14)
banco.adicionar_aluno("Cleiton dos Santos", "9°A", 15)
banco.adicionar_aluno("Fernando Pessoa", "9°A", 15)
banco.adicionar_aluno("Roberta francisca", "9°A", 14)

#turma 8°B
banco.adicionar_aluno("Gustavo Marques", "8°B", 13)
banco.adicionar_aluno("Gabrielly dos Santos", "8°B", 14)
banco.adicionar_aluno("Pedro Costa", "8°B", 13)
banco.adicionar_aluno("Maria Eduarda", "8°B", 13)
banco.adicionar_aluno("Mariana de Jesus", "8°B", 14)

banco.fechar()
print("\nBanco populado com sucesso!")