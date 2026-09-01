"""Agora faça um programa que:

Mostre o diretório atual;
Entre em teste;
Mostre novamente o diretório atual;
Liste os arquivos/pastas;
Entre em pasta1;
Mostre onde está"""

import os
path = os.path.join(os.getcwd(),'pasta_teste','Projeto','Backup')
print(path)
os.chdir(path)
if not os.path.exists('PastaTeste'):
    os.mkdir('PastaTeste')
path = os.path.join(os.getcwd(),'PastaTeste')
os.chdir(path)
if not os.path.exists('Teste1'):
    os.mkdir('Teste1')
if not os.path.exists('Teste2'):
    os.mkdir('Teste2')
if not os.path.exists('Teste3'):
    os.mkdir('teste3')
print(os.listdir(os.getcwd()))
path = os.path.join(path,'Teste1')
os.chdir(path)
print(os.listdir(os.getcwd()))