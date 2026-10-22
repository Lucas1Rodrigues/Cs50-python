from classes import *
from rich import print 

dist = 100000

t1 = Drone(dist)

print(f"O frete de {type(t1).__name__} custa R$: {t1.calc_frete()}")