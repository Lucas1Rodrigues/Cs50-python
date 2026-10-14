"""Dada a lista:
precos = [50, 120, 80, 200, 30, 150]



Faça duas operações:
1. Use filter() para selecionar preços maiores que 70.
2. Use map() para aplicar um desconto de 10% aos preços selecionados.
O resultado deve conter somente os preços selecionados, já com o desconto aplicado."""
precos = [50, 120, 80, 200, 30, 150]

precos70 = list(filter(lambda x : x>70, precos))
desconto = list(map(lambda x : x*0.9, precos70))
print(desconto)