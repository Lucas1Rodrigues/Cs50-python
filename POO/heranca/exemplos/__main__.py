from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
from rich import inspect

def main():
    prof1 = Professor("Rogério",77,"Ciencias politicas","Mestrado")
    inspect(prof1)

    aluno1 = Aluno("Lucas",27,"ADS","B")
    inspect(aluno1)

if __name__ == "__main__":
    main()








        
