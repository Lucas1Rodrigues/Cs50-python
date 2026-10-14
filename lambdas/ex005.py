"""onverter temperaturas

Dada a lista de temperaturas em Celsius:
celsius = [0, 20, 30, 37, 100]



Use map() e lambda para converter todas para Fahrenheit.
Fórmula: F = C * 9/5 + 32 """

celsius = [0, 20, 30, 37, 100]

farenheidt = list(map(lambda C : C * 9/5 + 32, celsius ))
print(farenheidt)
