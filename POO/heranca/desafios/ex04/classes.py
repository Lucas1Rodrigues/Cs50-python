from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
class Funcionario(ABC):
    def __init__(self,nome="",valorHora=0,horas=0,salarioBruto=0):
        super().__init__()
        self.nome = nome
        self.valorhora = valorHora
        self.hora = horas
        self.salarioBruto = salarioBruto
        self.salarioMinimo = 1800
        self.inss = 0.925
        self.salarioLiquido = self.salarioBruto * self.inss

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        return self.salarioLiquido/self.salarioMinimo

class Horista(Funcionario):
    def __init__(self, nome, horas, valorHora):
        super().__init__(nome=nome, horas=horas,valorHora=valorHora)

    def calc_sal(self):
        self.salarioBruto = self.hora * self.valorhora
        self.salarioLiquido = self.salarioBruto*self.inss
        print(Panel(f"O funcionário [yellow]{self.nome}[/] recebe R${self.salarioLiquido:.1f} por mês e R${self.valorhora} por hora, {self.analisar_sal():.1f} salários mínimos", title="HORISTA"))

class Mensalista(Funcionario):
    def __init__(self, nome="", salarioBruto=0):
        super().__init__(nome= nome,salarioBruto = salarioBruto)
        
    def calc_sal(self):    
        print(Panel(f"O funcionário [yellow]{self.nome}[/] recebe R${self.salarioLiquido:.1f} por mês e {self.analisar_sal():.1f} salários mínimos", title="Mensalista"))
    
        

        
