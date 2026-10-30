from hashlib import sha256
from rich import print
class ContaBancaria:
    def __init__(self,id='',titular='',saldo=0,senha=123):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__senha = None
        self.__hash = None

    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self,nome):
        if not isinstance(nome,str) and len(nome) > 0:
            raise ValueError("O nome do titular deve ser em Letras") 
        else:
            self._titular = nome  
 
    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self,senha):
        if len(senha) > 0:
            self.__hash = sha256(senha.encode('utf-8')).hexdigest
        else:
            raise ValueError("Senha inválida.")


    def validarSenha(self,senha):
        usuario = sha256(senha.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
           print("[green]Acesso permitido.[/]")
           return True
        else:
            print("Acesso Negado.")
            return False

    def new_method(self):
        return True

    def pedeSenha(self):
        print("[yellow]Digite sua senha: [/]")
        senhaInput = input()
        self.validarSenha(senhaInput)

    def sacar(self,saque,senha):
        if self.validarSenha(senha) == True:
            self.__saldo -= saque
        else:
            raise PermissionError("[red]Senha inválida.[/]")


    def depositar(self,deposito):
        if len(deposito) < 0 and not isinstance(deposito,int) and not isinstance(deposito,float):
            raise ValueError("Valor digitado nao é disponivel.")
        else:
            print("Deposito bem sucedido")
            self.__saldo += deposito