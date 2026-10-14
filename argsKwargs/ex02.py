"""ncontrar o maior número

Crie uma função maior_numero(*args) que retorne o maior número recebido.

Exemplos:

maior_numero(4, 9, 2) → 9

maior_numero(-5, -2, -10) → -2"""

def maior(*args):
    if len(args) == 0:
        return None
    maior = 0
    for num in args:
        if num > maior:
            maior = num
    return maior
print(maior(-1000,20,19))
