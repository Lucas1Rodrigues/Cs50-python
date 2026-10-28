from Aluno import Aluno
def main():
    al1 = Aluno("Lucas","Matematica",9.5)
    al1.nota = 8.6
    print(f"Nota de {al1.nome} em {al1.disciplina}: {al1.nota}")
    
    

if __name__ == "__main__":
    main()