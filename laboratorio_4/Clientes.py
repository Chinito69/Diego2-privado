from Persona import Persona
class Clientes(Persona):
    def __init__(self,nombre,rut,telefono,correo,horas_visitas,cariñosa_actual,habitacion_comun):
        super().__init__(nombre,rut,telefono,correo)
        self.__horas_visitas=horas_visitas
        self.__cariñosa_actual=cariñosa_actual
        self.__habitacion_comun=habitacion_comun
    ### get y set de horas por cada cariñosa
    def get_horas_visitas(self):
        return self.__horas_visitas
    def set_horas_visitas(self,horas_visitas):
        self.__horas_visitas=horas_visitas
    ### get y set de cariñosa actual
    def get_cariñosa_actual(self):
        return self.__cariñosa_actual
    def set_cariñosa_actual(self,cariñosa_actual):
        self.__cariñosa_actual=cariñosa_actual
    ###
    def get_habitacion_comun(self):
        return self.__habitacion_comun
    def set_habitacion_comun(self,habitacion_comun):
        self.__habitacion_comun=habitacion_comun
    ###
    def __str__(self):
        return super().__str__()+f"- Horas con la cariñosa: {self.__horas_visitas} - Cariñosa actual: {self.__cariñosa_actual} - Habitacion Comun: {self.__habitacion_comun}"