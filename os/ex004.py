import os
os.chdir('C:/Users/ACER/Documents/estudos/estudosPython/os/pasta_teste/Projeto/Codigo')
for n in range(1,6):
    if not os.path.exists(f"arquivo{n}.txt"):
        if not os.path.exists(f"text{n}.txt"):
            arquivo = open(f"text{n}.txt","w")
            arquivo.close()

for i in range(1,6):
    if os.path.exists(f"text{i}.txt"):
        os.rename(f"text{i}.txt",f"arquivo{i}.txt")

print(os.listdir(os.getcwd()))

