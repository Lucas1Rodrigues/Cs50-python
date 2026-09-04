"""
Exercícios em ordem crescente
1. Criar um arquivo
Crie um arquivo chamado teste.txt e escreva nele:
Olá, estou aprendendo Python!"""

with open("ex001.txt","w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, estou aprendendo Python!")