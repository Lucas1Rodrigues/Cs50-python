"""Crie uma classe onde podemos cadastrar nome e preco, e no final mostre uma
etiqueta do produto """
from rich.console import Console
from rich.table import Table

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        tabela = Table(title= "Produto")
        tabela.add_column("Nome", style="bold white")
        tabela.add_column("Preco", style="green")
        tabela.add_row(self.nome,f"R${self.preco:,.2f}")
        
        console = Console()
        console.print(tabela)

t1 = Produto("Iphone 15 pro max",12000)
t1.etiqueta()
        