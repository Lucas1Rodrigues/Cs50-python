from abc import ABC, abstractmethod
class Poligono(ABC):
    def __init__(self,qtd_lados = 0):
        self.qtd = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class quadrado(Poligono):
    def __init__(self,lado):
        super().__init__(4)
        self.lado = lado
        


    def perimetro(self):
        return self.lado*4
            

    def area(self):
        return self.lado*self.lado

class Circulo(Poligono):
    pi = 3.14151
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio
        

    def perimetro(self):
        return 2 * self.pi * self.raio

    def area(self):
        return self.pi * self.raio*self.raio


        


        