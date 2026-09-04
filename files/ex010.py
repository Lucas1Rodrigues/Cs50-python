with open("aluno1.txt", "r", encoding="utf-8") as arquivo1:
    with open("aluno2.txt", "r", encoding="utf-8") as arquivo2:
        with open("aluno3.txt", "r", encoding="utf-8") as arquivo3:
            with open("todos.txt", "w", encoding="utf-8") as arquivoT:

                arquivo = [arquivo1, arquivo2, arquivo3]

                for arquivo_atual in arquivo:
                    for line in arquivo_atual:
                        arquivoT.write(line)