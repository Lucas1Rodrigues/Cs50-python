"""Somar números com *args

Crie uma função chamada somar(*args) que receba qualquer quantidade de números e retorne a soma deles.

Exemplos de comportamento:

somar(2, 3) → 5

somar(1, 2, 3, 4) → 10

somar(10) → 10

Regra: a função também deve funcionar sem receber nenhum número."""

def somar(*args):
    total = 0
    for nums in args:
        total += nums
    return total

somar(1,2,3,4,5,6,7,8,9)
print(somar(1,2,3,4,5,6,7,8,9))