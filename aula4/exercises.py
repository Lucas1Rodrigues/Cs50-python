"""
#ex 1
aluno = {'nome': 'Lucas',
 'idade': 26,
  'curso': 'TI',
   'city': 'Itu-sp'
   }
print("Nome:", aluno.get('nome'))
print("Curso:", aluno.get('curso'))

#ex 02
aluno = {
	'nome': "Joao",
	"idade": 28
}
#[Chave] = "Item"
aluno['curso'] = "python"
aluno['nota'] = 8.5

print (aluno)


#ex 03
produto = {
    "nome": "Notebook",
    "preco": 3000,
    "estoque": 10
}

produto.update({"preco": 2800,
	"estoque": 15})
print(produto)


#ex 04

pessoa = {
    "nome": "Carlos",
    "idade": 25,
    "cidade": "Itu"
}

dadosUsuario = input("Digite a chave: ")
dadosUsuario = str(dadosUsuario)
print(pessoa.get(dadosUsuario,'Essa informação nao existe'))

#ex05
produtos = {
	'feijao': 9.90,
	'arroz': 15.00,
	'macarrao': 2.80,
	'cenoura': 5.20,
	'banana': 9.90
}
nome_removido = 'macarrao'
produtos_removidos = produtos.pop(nome_removido)
print("Produtos removidos: ", nome_removido)
print("produtos restantes: ", produtos.items())
"""