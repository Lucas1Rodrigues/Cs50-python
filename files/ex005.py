"""Crie um programa que conte quantas linhas existem em teste.txt.

Exemplo:

Quantidade de linhas: 2"""
n_linha = 0
with open("ex001.txt","r",encoding="utf-8") as arquivo:
    for linha in arquivo:
        n_linha += 1

print(f"Quantidade de linhas: {n_linha}")
