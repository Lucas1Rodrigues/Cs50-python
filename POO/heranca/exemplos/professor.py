from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome="", idade=0,materia="",nivel=""):
        super().__init__(nome, idade)
        self.materia = materia
        self.nivel = nivel
        

    def darAula(self):
        pass