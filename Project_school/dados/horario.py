HORARIOS = {
    "3": {"SEGUNDA": [
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
    "2": {
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
    {"aula": 2, "inicio": "07:50", "fim": "08:40"},
    {"aula": 3, "inicio": "09:00", "fim": "09:50"},
    {"aula": 4, "inicio": "09:50", "fim": "10:40"},
    {"aula": 5, "inicio": "11:30", "fim": "12:20"},
    {"aula": 6, "inicio": "12:20", "fim": "13:10"},
    {"aula": 7, "inicio": "13:10", "fim": "14:00"},

]

def get_aulas_do_dia(turma, dia_semana):
    """
  Mostra as aulas de uma turma em um dia específico.
    """
    import re
    turma = turma.lower().strip()
    turma = turma.replace("°","").replace("º","").replace("ano","").strip()
    turma = turma.replace(" ","")
    EXTENSO = {
        "terceiro": "3", "terceira": "3", "três": "3", "tres": "3",
        "segundo": "2", "segunda": "2", "dois": "2",
    }
    for extenso, digito in EXTENSO.items():
        turma = re.sub(rf"\b{extenso}\b", digito, turma)
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
def get_dia_relativo(relativo):
    """
    Retorna o dia da semana baseado em palavras comom hoje, amanhã, ontem, depois de amanhã
    """

    from datetime import datetime, timedelta
    dias = {
        0: "SEGUNDA",
        1: "TERÇA",
        2: "QUARTA",
        3: "QUINTA",
        4: "SEXTA",
        5: "SABADO",
        6: "DOMINGO"
    }

    relativo= relativo.lower()
    hoje = datetime.now()
    if "hoje" in relativo:
        dia = hoje
    elif "amanhã" in relativo or "amanha" in relativo:
        dia = hoje + timedelta(days=1)
    elif "ontem" in relativo:
        dia = hoje - timedelta(days=1)
    elif "depois de amanhã" in relativo or "depois de amanha" in relativo:
        dia = hoje +timedelta(days=2)
    elif "segunda" in relativo:
        dia = hoje
        while dia.weekday() != 0:
            dia += timedelta(days=1)
    elif "terça" in relativo or "terca" in relativo:
        dia = hoje
        while dia.weekday() != 1:
            dia += timedelta(days=1)
    elif "quarta" in relativo:
        dia = hoje
        while dia.weekday() != 2:
            dia += timedelta(days=1)
    elif "quinta" in relativo:
        dia = hoje
        while dia.weekday() != 3:
            dia += timedelta(days=1)
    elif "sexta" in relativo:
        dia = hoje
        while dia.weekday() != 4:
            dia += timedelta(days=1)
    else:
        dia = hoje

    return dias[dia.weekday()]
