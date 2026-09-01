import os
path ='C:/Users/ACER/Documents/estudos/estudosPython/os/pasta_teste/Projeto/documentos'
print(os.getcwd())

for root, subFolder, filename in os.walk(path):
    for folder in subFolder:
        print("pasta encontrado:",folder)