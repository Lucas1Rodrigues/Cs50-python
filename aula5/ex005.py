valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
valor3 = float(input("Valor 3: "))
valor4 = float(input("Valor 4: "))
valor5 = float(input("Valor 5: "))

if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1
    if maior < valor3:
        maior = valor3
        
