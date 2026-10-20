from rich import print
class Caneta:
    def __init__(self,cor):
        self.cor = cor
        self.destampada = False

    def escrever(self,texto):
        if self.destampada == True:
            if self.cor.lower() == "blue":
                print(f'[{self.cor}]{texto}[/]')
            elif self.cor.lower() == "red":
                print(f'[{self.cor}]{texto}[/]')
            elif self.cor.lower() == "green":
                print(f'[{self.cor}]{texto}[/]')
            else:
                print("Apenas as cores 'red' 'blue' e 'green' estao disponiveis!")
        else:
            print("Voce precisa destampar a caneta!")

    def destampar(self):
        self.destampada = True

    def quebrarLinha(self,num):
        for i in range(1,num):
            print('\n')

c1 = Caneta("red")
c2 = Caneta("green")
c3 = Caneta("blue")

c1.destampar()
c3.destampar()
c2.destampar()

c1.escrever("lorem ipsum decabitur principium nostro virum pater")
c1.quebrarLinha(2)
c2.escrever("On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish")