#aqui sobrescreveu o artigo existente
with open("text2.txt","w",encoding="UTF-8") as f:
    f_write = f.write("Teste, aqui eu escrevi um texto.")
#escreve no final do arquivo
with open("text2.txt","a",encoding="UTF-8") as f:
    f_write = f.write("Teste, aqui eu escrevi um texto.")
