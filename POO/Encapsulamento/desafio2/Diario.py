from rich import print
class Diario:
    def __init__(self,senha='581321BB'):
        self.__segredos = []
        self.__senha = senha

    def ler(self,senha):
        if senha == self.__senha:
            print("[green]Diário Liberado![/]")
            for n in self.__segredos:
                print(f"-{n}")
        else:
            raise PermissionError("Permissão negada. Tente novamente ou procure a senha com o administrador")
    
    def escrever(self,texto):
        return self.__segredos.append(texto)

    @property
    def senha(self):
        raise PermissionError("Voce nao tem permissao para acessar a senha!")
            
        
    
    
    