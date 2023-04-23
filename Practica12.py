import tkinter as tk
from Logica12 import Login
from tkinter import messagebox

class Interfaz:
    def __init__(self, ventana):
#1.Instanciamos un objeto ventana
        self.ventana=ventana
        self.ventana.title("Practica 11.3 Frames")
        self.ventana.geometry("800x600")

        titulo1 = tk.Label(ventana, text="Usuario:", font=("Helvetica",30))
        titulo1.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = tk.Entry(ventana, font=("Helvetica", 30))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        titulo2 = tk.Label(ventana, text="Contraseña:", font=("Helvetica", 30))
        titulo2.pack(fill=tk.X, padx=20, pady=5)
        self.contraseña = tk.Entry(ventana, show="*", font=("Helvetica", 30))
        self.contraseña.pack(fill=tk.X, padx=20, pady=10, )

        self.botonLog= tk.Button(ventana, text="Ingresar", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.verificar)
        self.botonLog.pack()
        
    def verificar(self):
        Usuario = self.usuario.get()
        Password = self.contraseña.get()
        login = Login(Usuario, Password)
        if login.login():
            mensaje = "Bienvenido, " + Usuario + "!"
        else:
            mensaje = "Revise sus datos e intente de nuevo."
            if login.login() == None:
                mensaje = "un dato esta vacio"

        # Mostrar un mensaje de bienvenida o error
        messagebox.showinfo("Resultado", mensaje)
            
        

ventana= tk.Tk()
interfaz_login=Interfaz(ventana)
ventana.mainloop()