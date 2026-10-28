class Termostato:
    def __init__(self,temperatura = 24):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura 

    @temperatura.setter
    def temperatura(self,temperatura):
        if temperatura % 0.5 != 0:
            raise ValueError("apenas valor de 0.5 por 0.5")
        if temperatura < 16:
            self.__temperatura = 16
        elif temperatura > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = temperatura
        
    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"