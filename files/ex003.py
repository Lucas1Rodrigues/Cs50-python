"""3. Adicionar texto

Acrescente uma segunda linha ao arquivo:

Esta é a segunda linha.

Importante: não apague o texto anterior."""

with open("ex001.txt","a",encoding="utf-8") as arquivo:
        arquivo.write("\nEsta é a segunda linha.")
        