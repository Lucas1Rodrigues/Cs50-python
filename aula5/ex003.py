nota1 = float(input("Valor 1: "))
nota2 = float(input("Valor 2: "))
nota3 = float(input("Valor 3: "))
nota4 = float(input("Valor 4: "))

media = ((nota1 + nota2 + nota3 + nota4)/4)

if media >= 7.0 :
    print("==================================")
    print("media: ", media)
    print("APROVADO")
    print("==================================")
else :
    print("==================================")
    print("media: ", media)
    exame = float(input("digite sua nota no exame: "))
    print("==================================")
    novaMedia = (media + exame)/2
    if novaMedia > 5.0:
        print("==================================")
        print("sua media final", novaMedia)
        print("PARABENS VOCE APROVADO  ")
        print("==================================")
    else:
        print("==================================")
        print("sua media final", novaMedia)
        print("reprovado")
        print("==================================")