import pandas as pd
df = pd.read_csv('tres.csv')
print(df.head())


#1.- Mostrando Columnas
print(df.info())

#2.- IMPRESIÓN DE 4 TIPOS


columnaR_V = df[['REGION', 'TipoViveroFt', 'TipoViveroFo', 'TipoViveroO', 'TipoViveroV',]]

columnaE_D = df[['Espec1', 'Espec2', 'Espec3', 'DIRECCION']]

print(columnaR_V)
print(columnaE_D)

#3.- Nombres Fantasías Vivero específicos de (PJ) + superficie en hectáreas


Columna_Nombres_Superficies = df[['NOMBREFANTASIAVIVERO', 'SUPERFICIEVIVEROS', 'SEXO']]

print(Columna_Nombres_Superficies)

columna_sexo = Columna_Nombres_Superficies[Columna_Nombres_Superficies['SEXO'] == 'PJ']

print(columna_sexo)

#4











