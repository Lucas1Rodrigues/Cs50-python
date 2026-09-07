def leiaFloat():
    while True:
        try:
            a = float(input('Digite numerador: '))
            b = float(input('Digite o denominador: '))
            r = a/b
        except ZeroDivisionError:
            print("Não se pode dividir um numero por zero")
            continue
        except (ValueError, TypeError):
            print('Erro: Digite um valor válido!')
            continue
        except Exception as erro:
            print(f'Erro identificado como : {erro}')
            continue
        else:
            print(f'Resultado: {r}')
            break
        finally:
            print("+============================================+")

"""Exercício 2 — Entrada numérica

Peça ao usuário um número inteiro usando input().

Se ele digitar algo como:

abc

o programa não deve quebrar. Deve mostrar uma mensagem avisando que a entrada é inválida.

Conceito: ValueError."""

def converter_inteiro(valor):
    try:
        inteiro = int(valor)
    except ValueError:
        print("Digite um valor valido!")
    else:
        return inteiro
    finally:
        print('operação completa em 3 2 1...')

"""Exercício 4 — Função que sempre finaliza

Crie uma função chamada abrir_arquivo(nome) que tente abrir um arquivo de texto.

Ela deve:

imprimir o conteúdo se o arquivo existir;

tratar FileNotFoundError;

usar finally para imprimir:"""

def abrir_arquivo(nome):
    try:
        with open(nome,'r',encoding="utf-8") as file:
            a = file.read()
    except FileExistsError:
        print("arquivo contem um erro ou nao esta abrindo")
    except FileNotFoundError:
        print("Arquivo nao encontrado")
    else:
        print(a)

"""Exercício 5 — Idade válida

Crie uma função chamada pedir_idade() que fique pedindo uma idade até o usuário informar um valor válido.

A função deve:

converter a entrada para inteiro;

tratar texto que não seja número;

rejeitar valores menores que zero;

rejeitar valores maiores que 120;

retornar a idade válida.

Dica: use while True."""

def PermitirIdade():
    while True:
        try:
            idade = float(input("digite sua idade: "))
            idade = int(idade)
            if idade < 18:
                print("Voce deve ter 18 ou mais para entrar")
                continue
        except (ValueError, TypeError):
            print("Digite um valor válido ")
            continue
        else:
            return idade
           
            

        



        
    
