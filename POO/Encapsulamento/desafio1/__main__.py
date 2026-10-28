from Termostato import Termostato
from rich import print, inspect
def main():
    t = Termostato()
    try:
        t.temperatura = 19.4
    except ValueError as e:
        print(f"Valor inválido: {e}")

    print(f"Valor do termostato esta em {t.temperatura}")


if __name__ == "__main__":
    main()