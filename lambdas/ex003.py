""""""

alunos = [
    ("Ana", 8.5),
    ("Bruno", 6.0),
    ("Carlos", 9.2),
    ("Diana", 7.5)
]

alunosOrdem = sorted(alunos,key= lambda x : x[1], reverse=True)
print(alunosOrdem)