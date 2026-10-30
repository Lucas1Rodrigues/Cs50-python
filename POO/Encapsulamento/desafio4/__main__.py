from retangulo import Retangulo
r = Retangulo()
try:
    r.medidas = (12,30)
except Exception as e:
    print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")

print(r.medidas)