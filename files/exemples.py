#aqui sobrescreveu o artigo existente
with open("text.txt","w",encoding="UTF-8") as f:
    f_write = f.write("Teste, aqui eu escrevi um texto.")
#escreve no final do arquivo
with open("text2.txt","a",encoding="UTF-8") as f:
    f_write = f.write("Teste, aqui eu escrevi um texto.")
#le os cinco blocos por vez e para quando acabar o arquivo
with open("text2.txt","r+",encoding="utf-8") as arquivo:
    while True:
        bloco = arquivo.read(5)
        print(bloco)

        if not bloco:
            break



