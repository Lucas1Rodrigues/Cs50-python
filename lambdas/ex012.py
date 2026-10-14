"""Crie uma função filtrar_lista(valores, condicao) que receba uma lista e uma função de condição.
Use filter() para retornar apenas os elementos que atendam à condição.
Teste com uma lambda que selecione números positivos e outra que selecione números maiores que 50."""
def filtrar_lista(lista,funcao):
    return list(filter(funcao,lista))

numeros = [1,2,3,4,5,6,7,8,9,10]
positivos = lambda x : x>0
que50 = lambda x : x>50

print(filtrar_lista(numeros,positivos))
print(filtrar_lista(numeros,que50))

