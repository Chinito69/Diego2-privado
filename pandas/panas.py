import pandas as pd
df=pd.read_csv("nba.csv")
print(df.head())

#1.mostrar columnas
print(df.info())

#mostar columnas
columnaN_T=df[["Name","Team","Number","Position","Age"]]
print(columnaN_T)