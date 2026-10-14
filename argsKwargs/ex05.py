"""Cadastro de usuário

Crie uma função cadastrar_usuario(nome, **kwargs).

nome é obrigatório.

kwargs pode receber informações adicionais, como idade, email e cidade.

A função deve exibir o nome e todas as informações adicionais.

Exemplo:

cadastrar_usuario("Carlos", idade=30, email="carlos@email.com")

Pense em como percorrer as informações extras."""

def cadastrarUser(nome,**kwargs):
    print(nome)
    for keys,values in kwargs.items():
        print(f"{keys}: {values}")





cadastrarUser("Carlos", idade=30, email="carlos@email.com", city="Sao paulo")