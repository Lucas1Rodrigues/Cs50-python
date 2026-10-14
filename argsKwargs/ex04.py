"""Média de notas

Crie uma função calcular_media(*notas) que receba qualquer quantidade de notas e retorne a média.

Exemplos:

calcular_media(7, 8, 9) → 8.0

calcular_media(10, 6) → 8.0

Trate o caso em que nenhuma nota for informada."""

def funcao_media(*args):
    try:
        totalSoma = 0
        cont = 0
        for num in args:
            totalSoma +=  num
            cont += 1
        media = totalSoma/cont
        
    except ValueError:
        print("Digite um valor válido")
    except ZeroDivisionError:
        print("Digite no minimo um valor")
    else:
        return media

print(funcao_media(10,10,10,10,10,10))
