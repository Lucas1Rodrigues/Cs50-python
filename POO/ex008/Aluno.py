class Aluno():

    def __init__(self,nome='',disciplina='',nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

        #metodos acessores
    def get_nota(self):
            return self._nota

    def set_nota(self,nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("Nota Inválida!")
            
