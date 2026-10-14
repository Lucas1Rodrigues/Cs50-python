"""Dada a lista:
nomes = ["ana", "bruno", "carlos", "diana"]



Use map() e lambda para transformar todos os nomes em letras maiúsculas.
Resultado esperado: ["ANA", "BRUNO", "CARLOS", "DIANA"]"""

nomes = ["ana", "bruno", "carlos", "diana"]
nomesMaiusculos = list(map(lambda x : x.upper(), nomes))

print(nomesMaiusculos)