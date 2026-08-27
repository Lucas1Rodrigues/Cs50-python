#Crie uma função eh_par(numero) que retorne True se o número for par e False se for ímpar.

def eh_par(num):
    if(num % 2 == 0):
        return True
    else:
        return False

print(eh_par(2))