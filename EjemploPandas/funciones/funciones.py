from clases.persona import Persona

def crea_diccionario(personas):
    p = Persona() #declaramos un objeto persona
    op = 1
    nombres = []
    apellidos = []
    edades = []
    while op == 1:
        p.SetNombre(input('Ingrese el nombre: '))
        p.SetApellido(input('Ingrese el apellido: '))
        p.SetEdad(input('Ingrese la edad: '))
        op = int(input('para continuar presione 1: '))
        nombres.append(p.GetNombre())
        apellidos.append(p.GetApellido())
        edades.append(p.GetEdad())
    personas['Nombre'] = nombres
    personas['Apellido'] = apellidos
    personas['Edad'] = edades
    return personas

        