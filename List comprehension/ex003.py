# apenas numeros pares
nums = [1,2,3,4,5,6,7,8,9,10]
mylist = []

mylist = [n for n in nums if n%2 == 0]

print(mylist)