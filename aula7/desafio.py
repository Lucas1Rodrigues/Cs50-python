"""Desafio final: crie uma função calculadora(a, b, operacao).

Ela deve aceitar:

"+" → soma
"-" → subtração
"*" → multiplicação
"/" → divisão

Exemplos:

calculadora(10, 5, "+")  # 15
calculadora(10, 5, "-")  # 5
calculadora(10, 5, "*")  # 50
calculadora(10, 5, "/")  # 2

Dica: nesse exercício você vai precisar juntar função + parâmetros + return + if/elif.

Se quiser estudar exatamente no estilo do vídeo, eu recomendo fazer 1 → 4 → 5 → 7 → 8 → 9 → 10 → 12, nessa ordem."""

def calculadora(num1,num2,operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1/num2
    else:
        return "operacao nao permitida use apenas ('+','-','*','/')"


print(calculadora(2,4,'*'))