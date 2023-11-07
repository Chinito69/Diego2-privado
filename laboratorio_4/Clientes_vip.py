from Clientes import Clientes
class Clientes_vip(Clientes):
    def __init__(self,nombre,rut,telefono,correo,horas_visitas,cariñosa_actual,membrecia,habitaciones_vip):
        super().__init__(nombre,rut,telefono,correo,horas_visitas,cariñosa_actual)
        self.__membrecia=membrecia
        self.__habitaciones_vip=habitaciones_vip
    ###
    def get_membrecia(self):
        return self.__membrecia
    def set_membrecia(self,membrecia):
        self.__membrecia=membrecia
    ###
    def get_habitaciones_vip(self):
        return self.__habitaciones_vip
    def set_habitaciones_vip(self,habitaciones_vip):
        self.__habitaciones_vip=habitaciones_vip
    ###
    def __str__(self):
        return super().__str__()+f"- Membrecia: {self.__membrecia} - Habitacion Vip: {self.__habitaciones_vip}"