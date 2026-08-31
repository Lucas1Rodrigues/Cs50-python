# ["ímpar", "par", "ímpar", "par", "ímpar"]  resultado esperado

nums = [1,2,3,5,6,75,3]
mylist = []

mylist = ["par" if n %2 == 0 else "impar" for n in nums]
print(mylist)