from Persona import Persona
class Guardias(Persona):
    def __init__(self,nombre,rut,telefono,correo,sueldo,horas):
        super().__init__(nombre,rut,telefono,correo)
        self.__horas=horas
        self.__sueldo=sueldo
    ### get y set de horas
    def get_horas(self):
        return self.__horas
    def set_horas(self,horas):
        self.__horas=horas
    ### get y set de sueldo
    def get_sueldo(self):
        return self.__sueldo
    def set_sueldo(self,sueldo):
        self.__sueldo=sueldo
    ###
    def Guardia():
        lista_guardia=[("Juan Pérez","12.345.678-9","555-123-4567","juan.perez@example.com","40h","100.000 clp"),
        ("Ana Rodríguez","23.456.789-0","555-234-5678","ana.rodriguez@example.com"),
        ("Luis González","34.567.890-1","555-345-6789","luis.gonzalez@example.com"),
        ("Marta Smith","45.678.901-2","555-456-7890","marta.smith@example.com"),
        ("Javier Pérez","56.789.012-3","555-567-8901","javier.perez@example.com"),
        ("Carla López","67.890.123-4","555-678-9012","carla.lopez@example.com"),
        ("Daniel García","78.901.234-5","555-789-0123","daniel.garcia@example.com")
        ("Isabel Fernández","89.012.345-6","555-890-1234","isabel.fernandez@example.com"),
        ("Pedro Rodríguez","90.123.456-7","555-901-2345""pedro.rodriguez@example.com"),
        ("Laura Martínez","01.234.567-8","555-012-3456","laura.martinez@example.com"),
        ("Carlos Sánchez","12.345.678-9","555-123-4567","carlos.sanchez@example.com"),
        ("Rosa Ramírez","23.456.789-0","555-234-5678","rosa.ramirez@example.com"),
        ("José López","34.567.890-1","555-345-6789","jose.lopez@example.com"),
        ("Elena González","45.678.901-2","555-456-7890","elena.gonzalez@example.com")
        ("Sergio Fernández","56.789.012-3","555-567-8901","sergio.fernandez@example.com")
        ("Carolina Pérez","67.890.123-4","555-678-9012","carolina.perez@example.com")
        ("Pablo Rodríguez","78.901.234-5","555-789-0123","pablo.rodriguez@example.com")
        ("Andrea Martínez","89.012.345-6","555-890-1234","andrea.martinez@example.com")
        ("Gabriel García","90.123.456-7","555-901-2345","gabriel.garcia@example.com")
        ("Sofia Smith","01.234.567-8","555-012-3456","sofia.smith@example.com")]
        return lista_guardia
    ###
    def __str__(self):
        return super().__str__()+f"- Horas: {self.__horas} - Sueldo: {self.__sueldo}"