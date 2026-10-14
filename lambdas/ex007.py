"""O filter() mantém apenas os elementos que passam em um teste.
Exercício 7
Filtrar números pares

Dada a lista:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



Use filter() e lambda para manter apenas os números pares.
Resultado esperado: [2, 4, 6, 8, 10]"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x : x%2 == 0, numeros))
print(pares)