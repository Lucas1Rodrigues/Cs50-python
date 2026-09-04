"""Crie três arquivos:

aluno1.txt
aluno2.txt
aluno3.txt

Cada arquivo deve conter o nome de um aluno.

Depois, faça um programa que abra os três arquivos e imprima os nomes na tela."""

with open("aluno1.txt","r",encoding="utf-8") as arquivo1:
    with open("aluno2.txt","r",encoding="utf-8") as arquivo2:
        with open("aluno3.txt","r",encoding="utf-8") as arquivo3:
            arquivo = [arquivo1,arquivo2,arquivo3]
            for line in arquivo:
                print(line.read())