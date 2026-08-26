valor = int(input("Qual valor: "))


if valor <= 0:
    valor = valor*(-1)
    print(valor)
else:
    print("valor ja é positivo")
