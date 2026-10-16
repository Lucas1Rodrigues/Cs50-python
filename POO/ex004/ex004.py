"""Crie uma classe churrasco que informe o numero de pessoas, quanto de carne deve comprar 
e quanto sera o total do valor de carne e o valor por pessoa

"""
from rich import print
from rich.panel import Panel
#considere
# preco da carne: R$ 89,99
# consumo padrao por pessoa: 400g

class churrasco:
    def __init__(self,titulo,quant):
        self.titulo = titulo
        self.quant = quant

    def calcular(self):
        totalKg = self.quant * 0.4
        totalValor = totalKg * 89.99
        totalPessoa = totalValor/self.quant
        
        print(Panel(f" Analisando o [magenta]{self.titulo}[/] com [yellow]{self.quant}[/] convidados\n Cada participante comera [green]0.4 kg[/] de carne e o kg da carne será [red]R$89.99[/]\n Recomendo comprar [green]{totalKg:.2f}[/] Kg de carne para aproveitar seu churrasco\n O custo total será de R$[blue]{totalValor:.2f}[/]\n Cada participante pagará R$[blue]{totalPessoa:.2f}[/]", title=self.titulo)   ) 

c1 = churrasco("Churras dos parças", 10)
c1.calcular()
