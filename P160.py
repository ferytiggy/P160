from tkinter import*
from tkinter.messagebox import*
from PIL import ImageTk, Image
from tkinter import filedialog
import webbrowser
import os

root = Tk()
root.minsize(650,650)
root.maxsize(850,850)

abrir_img = ImageTk.PhotoImage(Image.open("abrir.png"))
cerrar_img = ImageTk.PhotoImage(Image.open("guardar.png"))
render_img = ImageTk.PhotoImage(Image.open("render.jpg"))

nombre_de_archivo = Label(root, text="nombre del archivo")
nombre_de_archivo.place(relx=0.28, rely=0.03, anchor=CENTER)

campo_archivo = Entry(root)
campo_archivo.place(relx=0.46, rely=0.03, anchor=CENTER)

area_de_texto = Text(root, height=35, width=80)
area_de_texto.place(relx=0.5, rely=0.55, anchor=CENTER)

boton_abrir = Button(root, image=abrir_img)
boton_abrir.place(relx=0.05, rely=0.03, anchor=CENTER)

boton_guardar = Button(root, image=cerrar_img)
boton_guardar.place(relx=0.11, rely=0.03, anchor=CENTER)

boton_render = Button(root, image=render_img)
boton_render.place(relx=0.17, rely=0.03, anchor=CENTER)

root.mainloop()



