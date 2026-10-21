from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        super().__init__()

    def preparar(self):
        print("   (  (\n    )  )\n  ........\n  |      |]\n  |      | ]\n  |      |]\n  \\      /\n   `----'")
        print("----------- Iniciando o Preparo ----------- ")
        self.ferverAgua()
        self.misturar()
        self.servir()
        print("Bebida Pronta\n------------------------\n\n")

    def ferverAgua(self):
        print("1. Fervendo agua a 100 graus celsius")

    @abstractmethod
    def misturar(self): 
        pass

    @abstractmethod    
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Passando agua pressurizada pelo pó de café moido...")

    def servir(self):
        print("3. Servindo café...")

class cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. inserindo as ervas do cha na agua quente...")

    def servir(self):
        print("3. servindo chá quente...")

class leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Pressurindo leite pelo bico...")

    def servir(self):
        print("3. Servindo leite com café...")
    