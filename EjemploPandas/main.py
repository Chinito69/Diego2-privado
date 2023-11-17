from funciones.funciones import *
from funciones.pandas import *
from funciones.graficos import *

personas = {} #declaramos diccionario vacio
print(personas)
crea_diccionario(personas)
print(personas)
crea_archivo(personas) #tarea el script arrojará un error cuando se ingrese solo un registro, solucionelo
df = crea_data_frame()
grafica_bar_data_frame(df)
grafica_pie_data_frame(df)

# si usa este df para los gráficos, este no funcionará correctamente ya contemplará cada dato en el gráfico
df_simulado =simula_data()
print(df_simulado)