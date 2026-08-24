# using strings 

name = input("Qual seu nome: ")
lastName = input("Seu sobrenome: ")
city = input("Cidade onde voce mora atualmente: ")
work = input("Qual sua profissao: ")
hobby = input("hobby favorito: ")

complete_name = (name + ' ' + lastName).title
upper = complete_name.upper()
lower = complete_name.lower()
lenght = len(complete_name)

print("==================================")
print("           MEU PERFIL         ")
print("==================================")
print('Oi, meu nome é' + ' ' + complete_name)
print(f'Atualmente moro em : {city}.')
print(f'Trabalho com {work}.')
print(f'Gosto muito de {hobby}.')
print(upper)
print(lower)
print("quantidade de caracteres do nome: " + lenght)