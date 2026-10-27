from abc import ABC, abstractmethod
import random 
class Personagem(ABC):
    def __init__(self, nome="",vida=0,golpes=[]):
        self.nome = nome
        self.vida = vida 
        self.golpes = golpes

    def atacar(self, alvo,forca):
        pass
        
        

    def receberDano(self,dano):
        danoAtaque = random.randint(0,dano)
        self.vida -= danoAtaque

    @abstractmethod
    def curar():
        pass

class Guerreiro(Personagem):
    def __init__(self, nome='', vida=0):
        super().__init__(nome=nome, vida=vida)

    def curar(self):
        cura = ["colocando atadura","Magia de atena","achou um baú"]
        nomeCura = random.choice(cura)
        self.vida += random.randint(0,1000)
        print(f"{self.nome} curou-se com {nomeCura}")

    def atacar(self, alvo, forca):
        if :
            

    def receberDano(self, dano):
        return super().receberDano(dano)
        


class Mago(Personagem):
    def __init__(self, nome="", vida=0):
        super().__init__(nome=nome, vida=vida)

