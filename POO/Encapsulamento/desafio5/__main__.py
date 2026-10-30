from contaBancaria import ContaBancaria
from rich import inspect,print
c1 = ContaBancaria("11121","Lucas",1000,"Lucas123")
try:
    c1.depositar(200.214)
    
except Exception as e:
    print(f"[red]Aconteceu um erro do tipo {type(e).__name__}: {e} [/]")
print(c1.__str__())

