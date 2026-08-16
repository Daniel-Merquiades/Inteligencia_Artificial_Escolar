
from flask import Flask, jsonify, request, g
from flask_cors import CORS
import sqlite3
import sys
import os
import subprocess
import signal


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dados.horario import get_aulas_do_dia, get_dia_atual
from dados.cardapio import get_cardapio_do_dia, HORARIOS_REFEICAO
from dados.banco import normalizar_turma

app = Flask(__name__)
CORS(app)

processo_ia = None

@app.route('/ia/ligar', methods=['POST'])
def ligar_ia():
    global processo_ia
    if processo_ia and processo_ia.pool() is None:
        return jsonify ({"status": "ja_ligada", "mensagem": "IA já está rodando!"})
    caminho_main= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "main.py")
    processo_ia = subprocess.Popen(
        ['python', caminho_main],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    return jsonify({"status": "ligada", "mensagem": "IA iniciada com sucesso!"})
@app.route('/ia/desligar', methods = ['POST'])
def desligar_ia():
    global processo_ia
    if processo_ia and processo_ia.poll() is None:
        processo_ia.terminate()
        processo_ia = None
        return jsonify({"status": "desligada", "mensagem": "IA encerrada!"})
    return jsonify({"status": "ja_desligada", "mensagem": "IA já estava desligada!"})
@app.route('/ia/status', methods=['GET'])
def status_ia():
    global processo_ia
    ligada = processo_ia is not None and processo_ia.poll() is None
    return jsonify({"ligada": ligada})

# Caminho do banco
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dados", "escola.db")

def get_db():
    """Cria uma conexão nova por requisição."""
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Fecha a conexão ao fim de cada requisição."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

# ── ALUNOS ──────────────────────────────────────────
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    turma = request.args.get('turma', '')
    db = get_db()
    
    if turma:
        # Busca todos e filtra pela normalização
        todos = db.execute("SELECT * FROM alunos ORDER BY nome").fetchall()
        alunos = [a for a in todos if normalizar_turma(a['turma']) == turma.strip()]
    else:
        alunos = db.execute("SELECT * FROM alunos ORDER BY nome").fetchall()

    return jsonify([{
        "id": a['id'],
        "nome": a['nome'],
        "turma": a['turma'],
        "idade": a['idade']
    } for a in alunos])

@app.route('/alunos/buscar', methods=['GET'])
def buscar_aluno():
    nome = request.args.get('nome', '')
    if not nome:
        return jsonify([])
    db = get_db()
    alunos = db.execute(
        "SELECT * FROM alunos WHERE nome LIKE ? OR nome = ? ORDER BY nome",
        (f"%{nome}%", nome)
    ).fetchall()
    return jsonify([{
        "id": a['id'],
        "nome": a['nome'],
        "turma": a['turma'],
        "idade": a['idade']
    } for a in alunos])

# ── PRESENÇA ────────────────────────────────────────
@app.route('/presenca', methods=['GET'])
def ver_presenca():
    turma = request.args.get('turma', '3')
    from datetime import date
    hoje = date.today().strftime("%Y-%m-%d")
    db = get_db()
    chamada = db.execute("""
        SELECT alunos.nome, chamadas.presente
        FROM chamadas
        JOIN alunos ON chamadas.aluno_id = alunos.id
        WHERE chamadas.data = ?
        ORDER BY alunos.nome
    """, (hoje,)).fetchall()

    # Filtra pela turma normalizada
    todos = db.execute("SELECT * FROM alunos").fetchall()
    nomes_turma = {a['nome'] for a in todos if normalizar_turma(a['turma']) == turma.strip()}
    
    return jsonify([{
        "nome": c['nome'],
        "presente": c['presente']
    } for c in chamada if c['nome'] in nomes_turma])

# ── HORÁRIO ─────────────────────────────────────────
@app.route('/horario', methods=['GET'])
def ver_horario():
    turma = request.args.get('turma', '3')
    dia = get_dia_atual()
    aulas, erro = get_aulas_do_dia(turma, dia)
    if erro:
        return jsonify({"erro": erro})
    return jsonify(aulas)

# ── CARDÁPIO ────────────────────────────────────────
@app.route('/cardapio', methods=['GET'])
def ver_cardapio():
    dia = get_dia_atual()
    cardapio, erro = get_cardapio_do_dia(dia)
    if erro:
        return jsonify({"erro": erro})
    return jsonify({
        "dia": dia,
        "cafe": cardapio["cafe"],
        "almoco": cardapio["almoco"],
        "horario_cafe": HORARIOS_REFEICAO["cafe"],
        "horario_almoco": HORARIOS_REFEICAO["almoco"]
    })

if __name__ == '__main__':
    print("Servidor rodando em http://localhost:5000")
    app.run(debug=True, port=5000)