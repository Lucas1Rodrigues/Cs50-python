#Ler o arquivo inteiro

#Abra o teste.txt e imprima todo o conteúdo na tela.

with open("ex001.txt","r",encoding="utf-8") as arquivo:
    print(arquivo.read())