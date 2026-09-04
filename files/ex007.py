"""Faça um programa que copie de origem.txt para copia.txt somente as linhas que contêm a palavra Python."""
with open("origem.txt","r",encoding="utf-8") as arquivoR:
    with open("copia.txt","w",encoding="utf-8") as arquivoW:
        for line in arquivoR:
            if "Python" in line:
                arquivoW.write(line)
                