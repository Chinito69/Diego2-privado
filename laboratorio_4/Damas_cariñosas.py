from Persona import Persona
class Damas_cariñosas(Persona):
    def __init__(self,nombre,rut,telefono,correo,apodo,descripcion,sueldo,hora):
        super().__init__(nombre,rut,telefono,correo)
        self.__apodo = apodo
        self.__descripcion=descripcion
        self.__sueldo=sueldo
        self.__hora=hora
    ### get y set de apodo
    def get_apodo(self):
        return self.__apodo
    def set_apodo(self,apodo):
        self.__apodo=apodo
    ### get y set de descripcion
    def get_descripcion(self):
        return self.__descripcion
    def set_descripcion(self,descripcion):
        self.__descripcion=descripcion
    ### get y set de sueldo
    def get_sueldo(self):
        return self.__sueldo
    def set_sueldo(self,sueldo):
        self.__sueldo=sueldo
    ### get y set de horarios
    def get_hora(self):
        return self.__hora
    def set_hora(self,hora):
        self.__hora=hora
    ###
    def __str__(self):
        return super().__str__()+f"- Apodo: {self.__apodo} - Descripcion: {self.__descripcion} - Sueldo: {self.__sueldo} - Horas trabajadas: {self.__hora}"