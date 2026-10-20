"""crie a classe gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa, crie um metodo que permita mostrar a ficha desse gamer"""
from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self,nome,apelido):
        self.nome = nome
        self.apelido = apelido
        self.favoritos = []
        

    def add_jogos_favoritos(self,jogos):
        self.favoritos.append(jogos) 

    def ficha(self):
        texto = f'Nome real: [white on blue]{self.nome}[/]\nJogos favoritos:\n'
        for jogos in self.favoritos:
            texto += f":video_game: [blue]{jogos}[/]\n"

        print(Panel(texto,title=f"Jogador <{self.apelido}>"))

g1 = Gamer("Lucas Christian","KillerT")
g1.add_jogos_favoritos("god of war")
g1.add_jogos_favoritos("Red dead redemption 2")
g1.add_jogos_favoritos("GTA: San andreas")

g1.ficha()

g2 = Gamer("Sarah Bond", "Sarinha matata")
g2.add_jogos_favoritos("barbie")
g2.add_jogos_favoritos("pubg")
g2.add_jogos_favoritos("CROSSFIRE")

g2.ficha()
