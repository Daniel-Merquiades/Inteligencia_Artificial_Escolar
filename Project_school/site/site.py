# Servidor FLASK que irá conectar o site ao banco de dados

from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os 

# Adiciona a pasta raiz ao path para importar os módulos do projeto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dados.banco import Banco
from dados.horario import get_aulas_do_dia, get_dia_atual
from dados.cardapio import get_cardapio_do_dia, HORARIOS_REFEICAO

app = Flask(__name__)
CORS(app)  # possibilita o html chamar o servidor

banco = Banco()

#--Alunos--
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    """
  Retorna todos os alunos do banco.
    """
    turma = request.args.get('turma','')
    if turma:
        alunos = banco.listar_turma(turma)
    else:
        banco.cursor.execute("SELECT * FROM alunos ORDER BY nome")
        alunos = banco.cursor.fetchall()
    return jsonify([{
        "id": a[0],
        "nome": a[1],
        "turma": a[2],
        "idade": a[3]
    }for a in alunos])
@app.route('/alunos/buscar', methods=['GET'])
def buscar_aluno():
    """
  Busca o aluno pelo nome
    """
    nome = request.args.get('nome', '')
    if not nome:
        return jsonify([])
    resultados = banco.buscar_aluno(nome)
    return jsonify([{
        "id": a[0],
        "nome": a[1],
        "turma": a[2],
        "idade": a[3]
    }for a in resultados])

#--PRESENÇA--
@app.route('/presenca', methods=['GET'])
def ver_presenca():
    """
   Retorna a presença do dia de uma turma
    """
    turma = request.args.get('turma', '3')
    chamada = banco.ver_chamada(turma)
    return jsonify([{
        "nome": c[0],
        "presente": c[1]
    }for c in chamada])

#--HORÁRIO--
@app.route('/horario', methods=['GET'])
def ver_horario():
    """
  Retorna o horário das aulas de uma turma hoje.
    """
    turma = request.args.get('turma', '3')
    dia = get_dia_atual()
    aulas, erro = get_aulas_do_dia(turma, dia)
    if erro:
        return jsonify({"erro": erro})
    return jsonify(aulas)

#--CARDÁPIO--
@app.route('/cardapio', methods=['GET'])
def ver_cardapio():
    """
    Retorna o cardápio de hoje.
    """
    dia = get_dia_atual
    cardapio, erro = get_cardapio_do_dia(dia)
    if erro:
        return jsonify({"erro": erro})
    return jsonify({
        "dia": dia,
        "cafe": cardapio["cafe"],
        "almoco": cardapio["almoco"],
        "horario_cafe": HORARIOS_REFEICAO("cafe"),
        "horario_almoco": HORARIOS_REFEICAO("almoco")
    })
if __name__ == '__main__':
    print ("Servidor rodando em http://localhost:5000")
    app.run(debug=True, port=5000)
