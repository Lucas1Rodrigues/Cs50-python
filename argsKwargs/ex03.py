"""Exibir informações com **kwargs

Crie uma função mostrar_dados(**kwargs) que receba informações nomeadas e mostre cada chave e seu valor.

Exemplo de chamada:

mostrar_dados(nome="Ana", idade=25, cidade="São Paulo")

Saída esperada, em linhas separadas:

nome: Ana
idade: 25
cidade: São Paulo"""

def mostrar_dados(**dados):
    for chave,valor in dados.items():
        print(f"{chave}: {valor}\n")

mostrar_dados(nome="Ana", idade=25, cidade="São Paulo")

