class Retangulo:
    def __init__(self,base=1,altura=1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base
        
    @base.setter
    def base(self,base):
        if not isinstance(base,float) and not isinstance(base,int):
            raise ValueError ("Valor precisa ser um numero")
        if base < 0:
            raise ValueError("Valor precisa ser maior que 0")
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self,altura):
        if not isinstance(altura,float) and not isinstance(altura,int):
                raise ValueError("Valor precisa ser um numero")
        if altura < 0:
                raise ValueError("Valor precisa ser maior que 0")
        else:
                self._altura = altura

    @property
    def area(self):
        return self._base * self._altura

    @area.setter
    def area(self):
        raise PermissionError ("Valor nao pode ser acessado")


    @property
    def medidas(self):
        return f'Base: {self.base}\nAltura: {self.altura}\nArea:{self.area}'

    @medidas.setter
    def medidas(self,valores:tuple):
         self.base = valores[0]
         self.altura = valores[1]
       
        
        