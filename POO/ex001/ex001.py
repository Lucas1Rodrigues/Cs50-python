class Pessoa:
    def __init__(self,n = "vazio", i = 0, s = '', f = False): #metodo contrutor
        #atributos
        self.nome = n
        self.idade = i
        self.sexo = s
        self.faculdade = f

    #metodos
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        palavraEstudante = "Atualmente nao estudo"
        if self.faculdade == True:
            if self.sexo.lower() == 'm':
                palavraEstudante = "sou um estudante"
            elif self.sexo.lower() == 'f':
                palavraEstudante = "sou uma estudante"
                            
        print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos, {palavraEstudante}')

    def __str__(self):
            palavraEstudante = "Atualmente nao estudo"
            if self.faculdade == True:
                        if self.sexo.lower() == 'm':
                            palavraEstudante = "sou um estudante"
                        elif self.sexo.lower() == 'f':
                            palavraEstudante = "sou uma estudante"

            return f'Olá meu nome é {self.nome} e tenho {self.idade} anos, {palavraEstudante}'

objPessoa = Pessoa("Lucas Christian",26,'m',True)
print(objPessoa)
objPessoa1 = Pessoa("Jessica Ramos",59,'F',False)
objPessoa1.aniversario()
print(objPessoa1)
    