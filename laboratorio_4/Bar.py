class Bar():
    def __init__(self,bebidas,comidas,postres,valor):
        self.__bebidas=bebidas
        self.__comidas=comidas
        self.__postres=postres
        self.__valor=valor

    def get_bebidas(self):
        return self.__bebidas
    def set_bebidas(self,bebidas):
        self.__bebidas=bebidas
    
    def get_comidas(self):
        return self.__comidas
    def set_comidas(self,comidas):
        self.__comidas=comidas

    def get_postres(self):
        return self.__postres
    def set_postres(self,postres):
        self.__postres=postres

    def get_valor(self):
        return self.__valor
    def set_valor(self,valor):
        self.__valor=valor

    def __str__(self):
        return f"- Bebidas: {self.__bebidas} - Comidas disponibles: {self.__comidas} - Postres disponibles: {self.__postres} - Valor a pagar: {self.__valor}"