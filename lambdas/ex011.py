"""Criar uma função de transformação

Crie uma função transformar_lista(numeros, funcao) que receba uma lista e uma função como argumentos.
A função deve usar map() para aplicar a função recebida a cada número.
Teste passando uma lambda que multiplique os números por 3 e outra que some 10 a cada número."""
numeros = [1, 2, 3, 4, 5]

func3 = lambda x : x*3
func10 = lambda x : x + 10

def transformar_lista(lista,funcao):
    return list(map(funcao,lista))

print(transformar_lista(numeros,func3))
print(transformar_lista(numeros,func10))