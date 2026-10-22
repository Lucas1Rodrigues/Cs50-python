from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self,distancia = 0):
        self.distancia = distancia
        self.frete = 0
       

    @abstractmethod
    def calc_frete():
        pass

class Moto(Transporte):
    def calc_frete(self):
        self.frete = 0.5
        return self.frete * self.distancia

class Caminhao(Transporte):
    def calc_frete(self):
        self.frete = 1.5
        if self.distancia >= 50:
            return self.frete * self.distancia
        else:
            return "\n\nDistancia minima de 50 km."

class Drone(Transporte):
    def calc_frete(self):
        self.frete = 9.5
        if self.distancia <= 10:
            return self.frete * self.distancia
        else:
            return "\n\nDistancia máxima de 10km"
