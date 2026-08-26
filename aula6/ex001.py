"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

user = input("Usuario: ")
senha = input("digite sua senha: ")

while True:
    if user != senha:
        break
    else:
        print("========================================")
        print("usuario e senha nao podem ser iguais")
        user = input("Usuario: ")
        senha = input("digite sua senha: ")
        


        