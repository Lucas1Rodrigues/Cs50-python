nota1 = float(input("Valor 1: "))
nota2 = float(input("Valor 2: "))
nota3 = float(input("Valor 3: "))
nota4 = float(input("Valor 4: "))

media = ((nota1 + nota2 + nota3 + nota4)/4)

if media >= 5.0 :
    print("media: ", media)
    print("APROVADO")
else:
    print("media:", media)
    print("REPROVADO")