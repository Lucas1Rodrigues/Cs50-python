"""Dada a lista:
numeros = [1, 2, 3, 4, 5, 6, 7, 8]



Use filter() para selecionar os pares e map() para elevar cada um ao quadrado.
Resultado esperado: [4, 16, 36, 64]
Dica: primeiro filtre; depois transforme."""
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = list(filter(lambda x : x%2 == 0, numeros))
quadrados = list(map(lambda x : x*x, pares))
print(quadrados)