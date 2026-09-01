"""Crie um programa que mostre:

O diretório atual onde o Python está trabalhando.
Todos os arquivos e pastas dentro dele.

Funções que você provavelmente vai precisar explorar:

os.getcwd()
os.listdir()"""
import os
atualDirect = os.chdir("C:/Users/ACER/Documents/estudos")
print(os.listdir(atualDirect))
