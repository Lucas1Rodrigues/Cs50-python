"""Ler linha por linha

Leia o arquivo usando um for e imprima cada linha separadamente.

Tente evitar que apareçam linhas em branco extras."""
with open("ex001.txt","r",encoding="utf-8") as arquivo:
    for line in arquivo:
       print(line.strip())
            
        