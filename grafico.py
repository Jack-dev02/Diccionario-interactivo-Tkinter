from tkinter import *
from tkinter import ttk
#Esta es la ventana principal tkinter
ventana = Tk()
ventana.config(bg="#666") #Color de fondo
ventana.title("Especificacion rollos Extruder")#Titulo de la ventana
ventana.iconbitmap("icono1.ico")#icono de la ventana
imagen = PhotoImage(file="reyma2.png")#Fondo de la aplicacion
lblImagen = Label(ventana, image=imagen).place(relx=0, rely=0)#mostar fondo
ventana.geometry("820x600")#Tamaño de la ventana



#Este es el diccionario que contiene la informacion que buscara el usuario
rollos = {}

#Esta son las variables que se usaran en el programa
ingreso = StringVar()
respuesta = StringVar()

#Esta es la funcion que se ejecuta al presionar el boton buscar
def lista():
    nombre = ingreso.get()
    caja2.delete(0,END)

    if nombre in rollos:
        caja2.insert(0,rollos[nombre])
        
    else:
        caja2.insert(0,"No existe el rollo")



#Esta es la etiqueta
texto= Label(ventana, text="Escribe una clave de producto a buscar" , bg="#123", fg="#fff", font=("Msgothic",12))
texto.place(relx=0.25, rely=0.10, relwidth=0.50, relheight=0.06)#Posicion y tamaño de la etiqueta

#Esta es la caja de texto
caja1 = Entry(ventana, textvariable=ingreso, font=("Arial",12))
caja1.place(relx=0.4, rely=0.25, relwidth=0.20, relheight=0.06)

# Esta es la etiqueta del boton
boton = Button(ventana, text="BUSCAR",command=lista,bg="#873600", fg="white")
boton.place(relx=0.46, rely=.40)

#esta es la etiqiueta de la caja de texto de resulatdo
texto1= Label(ventana, text="Peso y Espesor", bg="#123", fg="#fff", font=("Msgothic",12))
texto1.place(relx=0.42, rely=0.55)

#esta es la caja de texto de resultado
texto2= Label(ventana,textvariable=respuesta, fg="blue")
texto2.place(x=200, y=260)
caja2 = Entry(ventana, bg="#6B7169", fg="white",font=("Comicbd",12))
caja2.place(relx=0.25, rely=0.63, relwidth=0.50, relheight=0.07)

#Este boton es para cerrar la ventana
boton = Button(ventana, text="Salir",font=("Msgothic",12), command=ventana.destroy).place(relx=0.90, rely=0.90)



ventana.mainloop()
