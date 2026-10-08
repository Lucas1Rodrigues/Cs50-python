"""Forma compacta de criar listas, dicionários e sets em uma linha.
O essencial: [expressão for item in lista if condição]

Crie lista com quadrados de 1 a 10
Filtre só os números pares de uma lista de 1 a 20
Crie lista com o tamanho de cada palavra em ["python", "é", "incrível"]
Crie dicionário {nome: len(nome)} para uma lista de nomes
Filtre palavras com mais de 4 letras de uma frase"""

#Crie lista com quadrados de 1 a 10

nums = [1,2,3,4,5,6,7,8,9,10]
quadrados = []

quadrados = [ n*n for n in nums]
print(quadrados)

#Filtre só os números pares de uma lista de 1 a 20
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pares = []

pares = [n for n in nums if n%2 == 0]
print(pares)

#Crie lista com o tamanho de cada palavra em ["python", "é", "incrível"]
nomes = ["python","e","incrivel"]
tamanho = []

tamanho = [len(n) for n in nomes]
print(tamanho)

acimaQuatro = [n for n in nomes if len(n)>4]
print(acimaQuatro)

#Crie dicionário {nome: len(nome)} para uma lista de nomes
lista = ["LUCAS", "MIGUEL", "ESTER"]
dicionario = {}

dicionario = {'nome': n for n in lista}
print(dicionario)
