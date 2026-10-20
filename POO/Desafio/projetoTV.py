"""Simular um controle remoto de uma TV com as srguintes funcionalidades:
    aumentar volume +
    diminuir volume -
    proximo canal >
    canal anterior <
    desligar @
    fechar programa 0
"""
from rich.panel import Panel
from rich import print 
class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 1

    def BotaoPower(self, entrada):
            if entrada == '@':
               return True
            if entrada == '@' and self.BotaoPower() == True:
                return False

    def volume(self,entrada):
        if entrada == '+':
            self.volume += 1
        elif entrada == '-':
            self.volume -= 1
            


    def canal(self,entrada):
        if entrada == '>':
                self.canal += 1
        elif entrada == '<':
                self.canal -= 1

    def execucaoTV(self):
        entrada = ''
        while True:
            try:
                if self.ligada == False:
                    print(Panel("[red]Tv desligada, digite '@' para ligar.[/]"))
                    entrada = input("CH 1 < > VOL + - : ")
                    if entrada == '@':
                         if self.BotaoPower(entrada) == True:
                              print("TV Ligada,\n canal [1] 2 3 4 5")
                              
                    
                         
                                             