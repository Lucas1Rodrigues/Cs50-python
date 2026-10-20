"""crie uma classe chamada livros para simular a passagem de paginas até o fim do livro"""
from time import sleep
from rich import print
class Livro:
    def __init__(self,totalPg):
        self.totalpg = totalPg
        self.paginaAtual = 1 
        print(f"Voce esta atualmente na página {self.paginaAtual}")

    def passar_Pagina(self, quant):
                cont = 0
                for pg in range(0,quant,1):
                      if not self.fimDoLivro():
                            self.paginaAtual += 1
                            print(f"Página{self.paginaAtual} :arrow_forward: ")
                            sleep(0.2)
                            cont += 1
                print(f"voce avancou {cont} páginas")
    def fimDoLivro(self):
         return True if self.totalpg == self.paginaAtual else False

livro = Livro(10)
livro.passar_Pagina(2)
livro.passar_Pagina(5)



                    
                
                

