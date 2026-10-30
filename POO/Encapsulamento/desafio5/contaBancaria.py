from hashlib import sha256
from rich import print
class ContaBancaria:
    def __init__(self,id='',titular='',saldo=0):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
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
            self.__hash = sha256(senha.encode('utf-8')).hexdigest()
        else:
            raise ValueError("Senha inválida.")


    def validarSenha(self,senha):
        usuario = sha256(senha.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
           return True
        else:
            return False


    def pedeSenha(self):
        print("[yellow]Digite sua senha: [/]")
        senhaInput = input()
        return senhaInput

    def sacar(self,saque):
        senhaInput = self.pedeSenha()
        if self.__saldo < saque:
            raise PermissionError("você nao tem fundos suficientes para o saque, verifique seu saldo")
        if self.validarSenha(senhaInput) == True:
            print(f'[green]Saque de {saque} bem sucedido[/]')
            self.__saldo -= saque
        else:
            print("[red]Senha inválida.[/]")


    def depositar(self,deposito):
        if deposito < 0:
            raise ValueError("Você nao pode depositar um válor negativo")
        if not isinstance(deposito,int) and not isinstance(deposito,float):
            raise ValueError("Valor digitado nao é disponivel.")
        else:
            print("Deposito bem sucedido")
            self.__saldo += deposito