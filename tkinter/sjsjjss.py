import tkinter
ventana=tkinter.Tk()
ventana.geometry("450x350")
etiqueta=tkinter.Label(ventana,text="Hola mundo",bg="blue")#bg para darle color a la etiqueta

def saludo():
    print("Hola")
def textoDeLaCaja():#esto se pone para que se guarde lo escrito en la caja de texto en la consola
    text20=cajaTexto.get()#esencialemnte se escribe asi
    print(text20)
boton1=tkinter.Button(ventana,text="Precioname",command=textoDeLaCaja,width=10,height=5).place(x=100,y=30)#esta funcion hace que se ponga lo que esta en la caja de texto en la consola y la parte de "width" o "height" se ocupa para agrandar los botones donde el "width" es la X y el "height" es la Y

#boton1=tkinter.Button(ventana,text="Precioname",command=saludo)#el comando pone lo que salga en la consola en este caso "hola"

#cajaTexto=tkinter.Entry(ventana,font="Arial 20") #la parte del font hace el porte de la letra, osea es como poner una letra de un word
cajaTexto=tkinter.Entry(ventana)
cajaTexto.pack()
#def saludo(nombre):
    #print("Hola" + nombre)#esta funcion pone el nombre con la parte del lamba 
#boton1=tkinter.Button(ventana,text="Precioname",command= lambda: saludo(python)) #pone la funcion en este caso hola y en la parte de "lambda: saludo(python)" y agrega hola y la parte que esta en el parentecis de saludo y todo lo printea a la consola

#boton1=tkinter.Button(ventana,text="Precioname",padx=40,pady=50)#si no quieres agrandar en los ejes x o y solo borra los "pad" ya sea el del x o y, esto es para el tamaño del boton


etiqueta.pack()#esta pone la etiqueta en el centro pero en la parte superior

#etiqueta.pack(side=tkinter.BOTOOM)#esta funcion pone la etiqueta abajo centro de la ventana

#etiqueta.pack(side=tkinter.RIGHT)#esta funcion pone la etiqueta a la derecha em la central de la ventana

#etiqueta.pack(fill=tkinter.X)#esta funcion pone a lo largo donde este la etiqueta con el color del bg

#etiqueta.pack(fill=tkinter.Y,expand=True)#esta funcion pone a lo ancho donde este la etiqueta con el color del bg 

#etiqueta.pack(fill=tkinter.BOTH,expand=True)#esta funcion pone en toda la pantalla del color del bg y pone la etiqueta en el centro de la ventana

ventana.mainloop()
#fill para ponerlo con el eje X e Y, y el side para ponerlo de abajo arriba o a la derecha