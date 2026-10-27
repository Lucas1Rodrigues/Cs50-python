class ContaBancaria:
    """Representa uma conta bancária de um cliente.
    Permite consultar saldo, depositar e sacar valores.
    Mantém o controle das movimentações financeiras."""
    def __init__(self,id,nome,saldo):
        self.id = id
        self._nome = nome
        self.__saldo = saldo

    def __str__(self):
        print("==========================")
        return f'Id:{self.id}; nome:{self._nome}; saldo R$ {self.__saldo:,.2f}'

    def depositar(self,valor):
        print("==========================")
        self.__saldo += valor
        print(f"deposito de {valor:,.2f} AUTORIZADO")
        
    def sacar(self,valor):
        print("==========================")
        if valor > self.__saldo:
            print(f"Saque de {valor} NEGADO, atual valor: {self.__saldo:,.2f} ")
        else:
            self.__saldo -= valor
            print(f"saque de {valor:,.2f} AUTORIZADO")


