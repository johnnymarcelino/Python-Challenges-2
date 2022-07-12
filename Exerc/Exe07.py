# coding: utf-8

# 7) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros.
# Em seguida, imprima os parâmetros recebidos na tela:

def variadica(*args):
    print(f"Os argumentos são: {args}")


variadica(4, "johnny", 49, True, False, "Marcelino")