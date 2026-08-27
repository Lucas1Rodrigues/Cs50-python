#Crie uma função chamada calcular_salario(salario, bonus).

#Ela deve receber o salário e o percentual de bônus e retornar o salário final.

def calculoBonus(salario,bonus):
    return (salario*bonus/100) + salario

print(calculoBonus(2000,10))