"""Exercício 8
Filtrar palavras

Dada a lista:
palavras = ["sol", "computador", "lua", "programacao", "mar"]



Use filter() e lambda para manter somente as palavras com mais de 4 caracteres."""
palavras = ["sol", "computador", "lua", "programacao", "mar"]

palavras4 = list(filter(lambda x: len(x)>=4, palavras))
print(palavras4)