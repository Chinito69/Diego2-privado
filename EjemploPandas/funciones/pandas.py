import pandas as pd
import random

nombres = ['Juan','Pedro','Maria','Helena','Carolina','Nelson','Leon']
apellidos = ['Díaz','Gonzalez','Lorca','Jara','Vidal','Catalan','Blanco']
edades = [50,35,18,12,72,80,5]


def random_indice():
    return random.randint(0, 6)

def crea_archivo(personas):
    dataframe = pd.DataFrame(personas)
    dataframe.to_excel('personas.xlsx')
    print('archivo creado con éxito')

def carga_archivo():
    df = pd.read_excel('personas.xlsx',names=['Nombres','Apellidos','Edades'])
    print('archivo cargado')
    return(df)

def crea_data_frame():
    df = carga_archivo()
    return df

def simula_data():
    n = []
    a = []
    e = []
    p = {}
    for i in range(50):        
        n.append(nombres[random_indice()])
        a.append(apellidos[random_indice()])
        e.append(edades[random_indice()])
    p['Nombres'] = n
    p['Apellidos'] = a
    p['Edades'] = e
    df_simulado = pd.DataFrame(p)
    return df_simulado


    

