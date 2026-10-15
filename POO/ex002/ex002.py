class ContaBancaria:
    """Representa uma conta bancária de um cliente.
    Permite consultar saldo, depositar e sacar valores.
    Mantém o controle das movimentações financeiras."""
    def __init__(self,id,nome,saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        print("==========================")
        return f'Id:{self.id}; nome:{self.nome}; saldo R$ {self.saldo:,.2f}'

    def depositar(self,valor):
        print("==========================")
        self.saldo += valor
        print(f"deposito de {valor:,.2f} AUTORIZADO")
        
    def sacar(self,valor):
        print("==========================")
        if valor > self.saldo:
            print(f"Saque de {valor} NEGADO, atual valor: {self.saldo:,.2f} ")
        else:
            self.saldo -= valor
            print(f"saque de {valor:,.2f} AUTORIZADO")


c1 = ContaBancaria(212,"Lucas Rodrigues",50000)

print(c1)
c1.sacar(45000)
print(c1)