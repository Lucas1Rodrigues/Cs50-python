"""Filtrar números

Crie uma função filtrar_pares(*args) que retorne uma lista contendo apenas os números pares recebidos.

Exemplo:

filtrar_pares(1, 2, 3, 4, 5, 6) → [2, 4, 6]

Tente resolver primeiro com um for. Depois, se quiser, experimente uma list comprehension."""

def filtrarPares(*args):
    if len(args) == 0:
        return None
    pares = []
    pares = [n for n in args if n%2 == 0 ]
    return pares

print(filtrarPares(1,2,34,5,6,77,5,32,2,23,4,5,63,2,1,1))