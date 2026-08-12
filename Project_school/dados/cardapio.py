CARDAPIO = {
    "SEGUNDA": {
        "cafe": "Pão com margarina e leite",
        "almoco": "Arroz, feijão, frango cozido, cenoura e salada de repolho. Sobremesa: banana"
    },
    "TERÇA": {
        "cafe": "Biscoito e leite com achocolatado",
        "almoco": "Arroz, feijão, carne moída com batata e abobrinha refogada. Sobremesa: laranja"
    },
    "QUARTA": {
        "cafe": "Pão com queijo e suco de fruta",
        "almoco": "Arroz, feijão, frango assado e macarrão ao molho de tomate. Sobremesa: melancia"
    },
    "QUINTA": {
        "cafe": "Bolo simples e leite",
        "almoco": "Arroz, feijão, carne em cubos com legumes e purê de batata. Sobremesa: banana"
    },
    "SEXTA": {
        "cafe": "Pão com margarina e vitamina de banana",
        "almoco": "Arroz, feijão, ovo mexido, macarrão com molho de tomate e salada de cenoura. Sobremesa: laranja"}
}
HORARIOS_REFEICAO = {
    "cafe": "8h40 às 09h00",
    "almoco": "10h40 às 11h30"
}

def get_cardapio_do_dia(dia_semana):
    """
  Retorna o cardápio de um dia específico.
    """
    dia_semana = dia_semana.upper()
    if dia_semana in ["SABADO", "DOMINGO"]:
        return None, "Fim de semana, não há refeições!"
    if dia_semana not in CARDAPIO:
        return None, f"Dia {dia_semana} inválido."
    return CARDAPIO[dia_semana], None