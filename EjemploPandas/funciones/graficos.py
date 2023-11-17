import matplotlib.pyplot as plt

def grafica_bar_data_frame(df):
    x = df['Nombres']
    y = df['Edades']
    fig, ax = plt.subplots()
    ax.bar(x = x, height = y)
    plt.show()

def grafica_pie_data_frame(df):
    nombres = df['Nombres']
    edades = df['Edades']
    #autopct indica el porcentaje para cada elemento
    plt.pie(edades,labels=nombres,autopct="%0.1f %%")
    plt.show()