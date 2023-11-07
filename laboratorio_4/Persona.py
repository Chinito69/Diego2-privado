class Persona():
    def __init__(self,nombre,rut,telefono,correo):
        self.__nombre=nombre
        self.__rut=rut
        self.__telefono=telefono
        self.__correo=correo
    ### get y set de nombres
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre=nombre
    ### get y set de rut
    def get_rut(self):
        return self.__rut
    def set_(self,rut):
        self.__rut=rut
    ### get y set de telefonos
    def get_telefono(self):
        return self.__telefono
    def set_telefono(self,telefono):
        self.__telefono=telefono
    ### get y set de correos
    def get_correo(self):
        return self.__correo
    def set_correo(self,correo):
        self.__correo=correo
    ### str o mostrar datos
    def __str__(self):
        return f"Nombre: {self.__nombre} - Rut: {self.__rut} - Telefono: {self.__telefono} - Correo: {self.__correo}"