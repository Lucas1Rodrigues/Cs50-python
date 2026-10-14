"""Mini projeto: processamento de vendas

Você recebeu os dados de vendas de uma loja:
vendas = [    {"produto": "Mouse", "preco": 80, "quantidade": 3},    {"produto": "Teclado", "preco": 150, "quantidade": 2},    {"produto": "Monitor", "preco": 900, "quantidade": 1},    {"produto": "Cabo", "preco": 25, "quantidade": 5},    {"produto": "Webcam", "preco": 200, "quantidade": 2}]



Crie funções para:
1. Usar filter() para selecionar produtos com preço acima de 100.
2. Usar map() para calcular o faturamento de cada produto (preco × quantidade).
3. Retornar os resultados em uma lista.
4. Exibir os resultados de maneira organizada.
Desafio extra: calcule o faturamento total dos produtos selecionados."""

vendas = [    
    {"produto": "Mouse", "preco": 80, "quantidade": 3},    
    {"produto": "Teclado", "preco": 150, "quantidade": 2},    
    {"produto": "Monitor", "preco": 900, "quantidade": 1},    
    {"produto": "Cabo", "preco": 25, "quantidade": 5},    
    {"produto": "Webcam", "preco": 200, "quantidade": 2}
    ]

produtos100 = list(filter(lambda x : x["preco"] >100,vendas))
faturamentoProduto = list(map(lambda x : x["preco"]*x["quantidade"], produtos100))


#for i in range(0,len(produtos100)):
   # print(f'{produtos100[i]["produto"]}: R${faturamentoProduto[i]}')  

for produto in produtos100:
    faturamento = produto["preco"]*produto["quantidade"]
    print(f'{produto["produto"]}: R${faturamento}')              
    

