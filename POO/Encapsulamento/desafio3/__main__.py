from credencial import Credencial

def main():
    c = Credencial()
    c.senha = input("Digite sua senha: ")
    print(c.senha)
    c.validar("Lucasdsjdhsuiasdf")




if __name__ == "__main__":
    main()