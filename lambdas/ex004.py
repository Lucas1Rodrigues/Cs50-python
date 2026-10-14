"""O map() aplica uma transformação a cada elemento.
Exercício 4
Dobrar uma lista

Dada a lista:
numeros = [1, 2, 3, 4, 5]



Use map() e lambda para gerar uma nova lista com todos os números dobrados.
Resultado esperado: [2, 4, 6, 8, 10]"""

numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x : x* 2 , numeros))
print(dobrados)