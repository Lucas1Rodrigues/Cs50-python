from contaBancaria import ContaBancaria
from rich import inspect,print
c1 = ContaBancaria("11121","Lucas",1000)
try:
    c1.senha = "Lucas"
    c1.depositar(100)
    c1.sacar(11000)
except Exception as e:
    print(f"[red]Aconteceu um erro do tipo {type(e).__name__}: {e} [/]")


