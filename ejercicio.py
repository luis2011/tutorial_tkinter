from tkinter import *

# importamos la base de datos SQlite
import sqlite3
conn = sqlite3.connect("personas.db")
cursor = conn.cursor()

ventana = Tk()
ventana.title ("Formularios")
ventana.geometry("700x400")

nombre = StringVar()
apellido = StringVar()
descripcion = StringVar()

#texto encabezado

encabezado = Label(ventana, text="Formularios con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("consolas", 18),
    padx=10,
    pady=10
)
#encabezado.pack(side="left", anchor=NW, fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=2, sticky=W)
# encabezado se pone la cantidad de columnas
# sticky=PEGALO EN..
# columnspan=2 , cantidad de columnas en mi grid


#label para el campo (nombre)
label= Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W, padx=5,pady=5)

#campos de texto(nombre)
campo_texto = Entry(ventana,textvariable=nombre)
campo_texto.grid(row=1, column=1, sticky=W,  padx=5,pady=5)
campo_texto.config(justify="left", state="normal")


#label para el campo (apellido)
label= Label(ventana, text="Apellidos")
label.grid(row=2, column=0, sticky=W, padx=5,pady=5)

#campos de texto(apellido)
campo_texto = Entry(ventana,textvariable=apellido)
campo_texto.grid(row=2, column=1, sticky=W,  padx=5,pady=5)
campo_texto.config(justify="left", state="normal")
#state nos da el estado del campus, habilitado o deshabilitado

#label para el campo (descripción - textArea)
label= Label(ventana, text="Descripción")
label.grid(row=3, column=0, sticky=N,padx=5,pady=5)

#campo de texto GRANDE(descripción)
campo_texto = Entry(ventana,textvariable=descripcion)
campo_texto.grid(row=3, column=1, sticky=W,  padx=5,pady=5)
campo_texto.config(justify="left", state="normal")




#crear botones

# creamos una separacion con el un label
Label(ventana).grid(row=4, column=1)

def agregar():
    db_nombre = nombre.get()
    db_apellido = apellido.get()
    db_descripcion = descripcion.get()
   
    #print(db_id)
    mostrar = f'Nombre: {db_nombre} Apellido {db_apellido} Dirección: {db_descripcion}' 

    conn.execute('''INSERT INTO usuarios (nombre,apellido,descripcion) VALUES('%s' , '%s' , '%s' )'''%(db_nombre,db_apellido,db_descripcion))

    conn.commit()


    #print("Registro insertado con exito")
    #limpiar campos
    nombre.set("")
    apellido.set("")
    descripcion.set("")

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
    padx=10,
    pady=15,
    bg="green",
    fg="white",
    command=agregar)




ventana.mainloop()
