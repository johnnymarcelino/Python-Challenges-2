# coding: utf-8

# 5) Escreva uma função que contenha dois parâmetros.
# O primeiro deve ser obrigatório e o segundo facultativo:


def dois_param(obrig, facult=""):
    print(obrig)
    print(facult)


dois_param("mensagem obrigatória", "somente se desejar")