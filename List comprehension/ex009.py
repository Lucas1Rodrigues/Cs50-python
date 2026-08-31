#criar um dicionario, cada numero é a chave e o quadrado é o conteudo

nums = [1,2,3,4,5,6,7]
myStruct = {}

myStruct = {n: n*n for n in nums}
print(myStruct)