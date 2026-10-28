class Aluno():

    def __init__(self,nome='',disciplina='',nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

        #metodoso acessores
        @property
        def nota(self):
            return self._nota   #getter
        
        @nota.setter
        def nota(self,nota): #setter
            if 0 <= nota <= 10:
                self._nota = nota
            else:
                print("Nota Inválida!")


        
 