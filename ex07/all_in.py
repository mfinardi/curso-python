# -*- coding: utf-8 -*-

import re

estados = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}

capitais = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def detectar_tipo_expressao(expressao):
    expressao = expressao.strip()  # Remove espaços em branco
    if expressao.upper() in [cidade.upper() for cidade in capitais.values()]:
        return "capital"
    elif expressao.title() in estados.keys():
        return "estado"
    else:
        return "nenhum"

def main():
    entrada = raw_input("Digite o texto contendo as expressões separadas por vírgula: ")
    if ",," in entrada:  # Verifica se há vírgulas consecutivas
        print("Erro: vírgulas consecutivas não são permitidas.")
        return

    expressoes = re.split(r',\s*', entrada)  # Divide a entrada em expressões separadas por vírgula
    for expr in expressoes:
        tipo_expr = detectar_tipo_expressao(expr)
        if tipo_expr == "capital":
            estado = [estado for estado, cidade in capitais.items() if cidade.upper() == expr.upper()][0]
            print("{} é a capital de {}".format(capitais[estado], estado))
        elif tipo_expr == "estado":
            cidade_capital = capitais[estados[expr.title()]]
            print("{} é a capital de {}".format(cidade_capital, estados[expr.title()]))
        else:
            print("{} não é uma capital nem um estado".format(expr))

if __name__ == "__main__":
    main()
