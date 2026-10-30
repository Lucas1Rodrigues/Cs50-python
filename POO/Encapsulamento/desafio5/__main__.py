from contaBancaria import ContaBancaria
from rich import inspect
c1 = ContaBancaria("11121","Lucas",1000)
inspect(c1,private=True,methods=True)