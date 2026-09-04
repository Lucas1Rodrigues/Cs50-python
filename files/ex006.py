"""6. Copiar o conteúdo
Crie dois arquivos:
origem.txt
copia.txt
Coloque algum texto em origem.txt e faça um programa que copie seu conteúdo para copia.txt."""

with open("origem.txt","r",encoding="utf-8") as arquivo:
    with open("copia.txt","w",encoding="utf-8") as arquivoW:
        for line in arquivo:
            arquivoW.write(line)

    