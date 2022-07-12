# coding: utf-8

# 04) Escreva um algoritmo contendo uma função que necessite de três argumentos.
# Em seguida, imprima na tela os argumentos em ordem ascendente e, por fim, imprima a média aritmética

def tre_args(a, b, c):
    ascendente = [a, b, c]
    ascendente.sort()
    print(ascendente)
    med_art = (a+b+c)/3
    print(f"a média aritmética é: {med_art}")


tre_args(7, 5, 9)