# coding: utf-8

# 7) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros.
# Em seguida, imprima os parâmetros recebidos na tela:

def variádica(*args):
    print(f"Os argumentos são: {args}")


variádica(4, "johnny", 49, True, False, "Marcelino")