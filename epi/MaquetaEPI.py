import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

def calcular_eficiencia():
    estado = estado_var.get()
    
    if estado == "Gaseoso":
        kg_h = kg_h_var.get()
        tiempo = tiempo_var.get()
        
        try:
            kg_h = float(kg_h)
            tiempo = float(tiempo)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos.")
            return
        if kg_h <= 0 or tiempo <= 0:
            messagebox.showerror("Error", "Ingresa valores mayores que cero.")
            return
        else: 
            eficiencia = kg_h * tiempo * 30
            eficiencia_str = "{:.2f} Kgh/mes".format(eficiencia)
            nota = obtener_nota(eficiencia)
            mensaje = "Eficiencia energética: {}\nNota de eficiencia: {}".format(eficiencia_str, nota)
            messagebox.showinfo("Resultado", mensaje)
        
    elif estado == "Líquido":
        litros_h = litros_h_var.get()
        tiempo = tiempo_var.get()

        try:
            litros_h = float(litros_h)
            tiempo = float(tiempo)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos.")
            return
        if litros_h <= 0 or tiempo <= 0:
            messagebox.showerror("Error", "Ingresa valores mayores que cero.")
            return
        else: 
            eficiencia = litros_h * tiempo * 30
            eficiencia_str = "{:.2f} Lh/mes".format(eficiencia)
            nota = obtener_nota(eficiencia)
            mensaje = "Eficiencia energética: {}\nNota de eficiencia: {}".format(eficiencia_str, nota)
            messagebox.showinfo("Resultado", mensaje)
        
def obtener_nota(eficiencia):                           
    if eficiencia <= 73:
        return "A"
    elif eficiencia <= 110:
        return "B"
    elif eficiencia <= 145:
        return "C"
    elif eficiencia <= 181:
        return "D"
    elif eficiencia <= 217:
        return "E"
    elif eficiencia <= 240:
        return "F"
    else:
        return "G"

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Eficiencia Energética")
ventana.geometry("1280x560")
ventana.configure(bg="#2A2A2A")


# Variables de control
estado_var = tk.StringVar(ventana)
kg_h_var = tk.StringVar(ventana)
litros_h_var = tk.StringVar(ventana)
tiempo_var = tk.StringVar(ventana)
#Fonts
Helvetica = tkFont.Font(family="Helvetica", size=46, weight="bold", slant="roman")
Helvetica2 = tkFont.Font(family="Helvetica", size=24, weight="bold", slant="roman")
Helvetica3 = tkFont.Font(family="Helvetica", size=18, weight="bold", slant="roman")

# Label bienvenida

wel =tk.Label(ventana,text="¡Bienvenido a Green Tracker!")
wel.configure(fg="#FFFFFF")
wel.configure(bg="#2A2A2A")
wel.place(x=215,y=1)

wel2 =tk.Label(ventana,text="Green Tracker")
wel2.configure(fg="#07e628")
wel2.configure(bg="#2A2A2A")
wel2.place(x=628,y=1)


wel.configure(font=Helvetica)
wel2.configure(font=Helvetica)

# Escoger una medicion
etiqueta_estado =tk.Label(ventana,text="Elige el tipo de hidrogeno verde:")
etiqueta_estado.configure(fg="#FFFFFF")
etiqueta_estado.configure(bg="#2A2A2A")
etiqueta_estado.place(x=30,y=200)
etiqueta_estado.configure(font=Helvetica2)



# Etiqueta y opción para seleccionar el estado

opcion_estado = tk.OptionMenu(ventana, estado_var, "Gaseoso", "Líquido")
opcion_estado.configure(bg="#4a4a4a")
opcion_estado.configure(fg="#FFFFFF")
opcion_estado.configure(font=Helvetica3)

opcion_estado.configure(height=1, width=20)
opcion_estado.place(x=34,y=250)

# Entradas para el estado gaseoso

etiqueta_kg_h = tk.Label(ventana, text="Kilogramos (kg):")
etiqueta_kg_h.configure(bg="#2A2A2A")
etiqueta_kg_h.configure(fg="#FFFFFF")
etiqueta_kg_h.configure(font=Helvetica3)

entrada_kg_h = tk.Entry(ventana, textvariable=kg_h_var)
entrada_kg_h.configure(width=47)


etiqueta_tiempo = tk.Label(ventana, text="Tiempo diario de uso (horas):")
etiqueta_tiempo.configure(bg="#2A2A2A")
etiqueta_tiempo.configure(fg="#FFFFFF")
etiqueta_tiempo.configure(font=Helvetica3)

entrada_tiempo = tk.Entry(ventana, textvariable=tiempo_var)
entrada_tiempo.configure(width=47)





# Entrada para el estado líquido
etiqueta_litros_h = tk.Label(ventana, text="Litros (L):")
etiqueta_litros_h.configure(bg="#2A2A2A")
etiqueta_litros_h.configure(fg="#FFFFFF")
etiqueta_litros_h.configure(font=Helvetica3)

entrada_litros_h = tk.Entry(ventana, textvariable=litros_h_var)
entrada_litros_h.configure(width=47)

# Botón de cálculo
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_eficiencia)
boton_calcular.configure(fg="#000000")
boton_calcular.configure(bg="#07e628")
boton_calcular.configure(height = 2, width = 15)
boton_calcular.configure(font=Helvetica3)


# Mostrar las entradas correspondientes al estado seleccionado
def mostrar_entradas():
    estado = estado_var.get()
    
    if estado == "Gaseoso":

        etiqueta_tiempo.place(x=34,y=340)
        entrada_tiempo.place(x=34,y=380)

        etiqueta_kg_h.place(x=34,y=420)
        entrada_kg_h.place(x=34,y=460)

        etiqueta_litros_h.place_forget()
        entrada_litros_h.place_forget()
    elif estado == "Líquido":

        etiqueta_tiempo.place(x=34,y=340)
        entrada_tiempo.place(x=34,y=380)

        etiqueta_litros_h.place(x=34,y=420)
        entrada_litros_h.place(x=34,y=460)

        etiqueta_kg_h.place_forget()
        entrada_kg_h.place_forget()
    
estado_var.trace("w", lambda *args: mostrar_entradas())

# Mostrar elementos iniciales
mostrar_entradas()
boton_calcular.place(x=780,y=340)

# Ejecutar la ventana principal
ventana.mainloop()