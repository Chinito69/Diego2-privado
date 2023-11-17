class Persona:
    def __init__(self,n='',a='',e=''):
        self.__nombre = n
        self.__apellido = a
        self.__edad = e
    
    def GetNombre(self):
        return self.__nombre
    def GetApellido(self):
        return self.__apellido
    def GetEdad(self):
        return self.__edad

    def SetNombre(self,n):
        self.__nombre = n
    def SetApellido(self,a):
        self.__apellido = a
    def SetEdad(self,e):
        self.__edad = e
