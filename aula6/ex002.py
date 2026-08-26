"""3. Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

nome = input("DIgite seu nome: ")
idade = int(input("Digite sua idade"))
salario = float(input("digite seu salario"))
sexo = input("DIgite seu sexo M ou F")
civil = input("Digite seu estado civil: ('s', 'c', 'v', 'd')")

while True:
    if(len(nome) < 3):
       print("Nome tem que ser acima de 3 caracteres")
       break
    elif not (idade > 0 and idade < 120):
        print("idade tem ser  entre 0 e 120")
        break
    elif (salario < 0):
        print("Salario tem quer maior que 0")
        break
    elif sexo.lower() not in ['f','m']:
        print("apenas f ou m")
        break
    elif civil.lower() not in ['s', 'c', 'v', 'd']:
        print("apenas 's', 'c', 'v', 'd'")
        break


                
                
    

