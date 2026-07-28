HORARIOS = {
    "9A": {"SEGUNDA": [
            "Matemática",
            "Matemática",
            "Português",
            "Português",
            "História",
            "História",
            "Educação Física",
        ],
        "TERÇA": [
            "Ciências",
            "Ciências",
            "Inglês",
            "Inglês",
            "Geografia",
            "Informática",
            "Informática",
        ],
        "QUARTA": [
            "Português",
            "Português",
            "Matemática",
            "Matemática",
            "Ciências",
            "História",
            "Geografia",
        ],
        "QUINTA": [
            "Inglês",
            "Inglês",
            "Educação Física",
            "Educação Física",
            "Português",
            "Matemática",
            "Matemática",
        ],
        "SEXTA": [
            "Geografia",
            "Geografia",
            "História",
            "Ciências",
            "Informática",
            "Informática",
            "Português",
        ],
},
    "8B": {
        "SEGUNDA": [
            "Português",
            "Português",
            "Ciências",
            "Ciências",
            "Matemática",
            "Inglês",
            "Inglês",
        ],
        "TERÇA": [
            "História",
            "História",
            "Geografia",
            "Geografia",
            "Português",
            "Português",
            "Educação Física",
        ],
        "QUARTA": [
            "Matemática",
            "Matemática",
            "Inglês",
            "Inglês",
            "História",
            "Ciências",
            "Informática",
        ],
        "QUINTA": [
            "Ciências",
            "Ciências",
            "Português",
            "Português",
            "Geografia",
            "Matemática",
            "Matemática",
        ],
        "SEXTA": [
            "Informática",
            "Informática",
            "Educação Física",
            "Educação Física",
            "Inglês",
            "História",
            "Geografia",
        ],
    }
}

PERIODOS = [
    {"aula": 1, "inicio": "07:00", "fim": "07:50"},
    {"aula": 2, "inicio": "07:00", "fim": "08:40"},
    {"aula": 3, "inicio": "07:00", "fim": "09:50"},
    {"aula": 4, "inicio": "07:00", "fim": "10:40"},
    {"aula": 5, "inicio": "07:00", "fim": "12:20"},
    {"aula": 6, "inicio": "07:00", "fim": "13:10"},
    {"aula": 7, "inicio": "07:00", "fim": "14:00"},

]

def get_aulas_do_dia(turma, dia_semana):
    """
  Mostra as aulas de uma turma em um dia específico.
    """
    turma = turma.upper()
    dia_semana = dia_semana.upper()

    if turma not in HORARIOS:
        return None, f"Turma {turma} não encontrada."
    if dia_semana not in HORARIOS[turma]:
        return None, f"Dia {dia_semana} inválido."

    materias = HORARIOS[turma][dia_semana]
    aulas = []
    for i, periodo in enumerate (PERIODOS):
        aulas.append({"aula": periodo ["aula"],"inicio": periodo["inicio"],"fim": periodo["fim"], "materia": materias[i]})
        return aulas, None
def get_dia_atual():
   """
 Retorna o dia da semana atual em portugês.
   """
   from datetime import datetime
   dias = {
       0:"SEGUNDA",
       1:"TERÇA",
       2:"QUARTA",
       3:"QUINTA",
       4:"SEXTA",
       5:"SABADO",
       6:"DOMINGO"
   }
   return dias[datetime.now().weekday()]
        