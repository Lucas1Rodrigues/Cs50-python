"""Ou seja:
pega apenas os pares
calcula o quadrado deles
Esse exercício é importante porque você precisa entender a diferença entre:
O QUE eu quero colocar na lista
e
QUAIS elementos devem entrar"""

nums = [1,2,3,4,5,6,7,8,9,10]
mylist = []

mylist = [n*n for n in nums if n%2 == 0]
print(mylist)