# apenas palavras com mais de 5 caracteres
nomes = ["Ana", "João", "Alexandre", "Maria", "José", "Fernando"]
mylist = []

mylist = [letter for letter in nomes if len(letter) > 5]
print(mylist)