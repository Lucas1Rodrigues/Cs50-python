from hashlib import sha256
from credencial import Credencial
class Credencial:
    def __init__(self):
        
        self.__hash = None

    @property
    def senha(self):
        return self.__hash
    
    @senha.setter
    def senha(self,chave):
        self.senha = sha256(chave.encode('utf-8')).hexdigest()

    def validar(self,chave):
        if chave == self.senha:
            print("[green]ACESSO LIBERADO![/]")
        else:
            print("[red]ACESSO NEGADO![/]")
        