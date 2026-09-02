import os
path ='C:/Users/ACER/Documents/estudos/estudosPython/'

for root, subFolder, filename in os.walk(path):
    for f in filename:
       if f.endswith(".py"):
           print("Documento: ", f)