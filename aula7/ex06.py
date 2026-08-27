#. Crie uma função maior(a, b) que receba dois números e retorne o maior deles.

def maior(num1,num2):
    if(num1 > num2):
        return num1
    else:
        return num2

maior = maior(2,3)
print(maior)