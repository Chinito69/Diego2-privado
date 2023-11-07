from Persona import Persona
from Guardias import Guardias
from Clientes import Clientes
from Clientes_vip import Clientes_vip
from Damas_cariñosas import Damas_cariñosas
lista_cliente=[]
lista_cliente_vip=[]
class Burdel():
    def crear_persona():
        nombre=input("Ingrese su nombre: ")
        rut=int(input("Ingrese su rut: "))
        telefono=input("Ingrese su numero telefonico: ")
        correo=input('Ingrese su correo electronico: ')
        return nombre,rut,telefono,correo
    ###
    def crear_cliente():
        nombre,rut,telefono,correo=Burdel.crear_persona()
        hora_visitas=int(input("Ingrese las horas que va a estar con la cariñosa: "))
        cariñosa_actual=""


    def crear_cliente_vip():
        nombre,rut,telefono,correo=Burdel.crear_persona()
