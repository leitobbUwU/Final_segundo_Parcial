from Logica13 import *
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.geometry("500x300")
        ventana.title("Generador de contraseñas")

        # Largo Contraseña
        self.largoContra= tk.Frame(ventana)
        self.largoContra.pack(padx=10, pady=5, fill=tk.X)

        self.titulo = tk.Label(self.largoContra, text="Largo de la contraseña:")
        self.titulo.pack(side=tk.LEFT)

        self.largoVar = tk.StringVar(value="8")
        self.largoC = tk.Entry(self.largoContra, textvariable=self.largoVar)
        self.largoC.pack(side=tk.LEFT, padx=(5, 0))

        # Incluir Mayusculas
        self.MayusculasCon = tk.Frame(ventana)
        self.MayusculasCon.pack(padx=10, pady=5, fill=tk.X)

        self.MayusVar = tk.BooleanVar(value=True)
        self.MAyusChec = tk.Checkbutton(self.MayusculasCon, text="Agregar mayusculas",
                                                 variable=self.MayusVar)
        self.MAyusChec.pack(side=tk.LEFT)

        # Incluir Caracteres Especiales
        self.EspecialesCon = tk.Frame(ventana)
        self.EspecialesCon.pack(padx=10, pady=5, fill=tk.X)

        self.especialVar = tk.BooleanVar(value=True)
        self.especialChe = tk.Checkbutton(self.EspecialesCon, text="Incluir Caracteres especiales", variable=self.especialVar)
        self.especialChe.pack(side=tk.LEFT)

        self.numerosCon = tk.Frame(ventana)
        self.numerosCon.pack(padx=10, pady=5, fill=tk.X)

        self.numerosVar = tk.BooleanVar(value=True)
        self.numerosChe = tk.Checkbutton(self.numerosCon, text="Incluir numeros", variable=self.numerosVar)
        self.numerosChe.pack(side=tk.LEFT)

        # Crear contraseña boton
        self.ContraseñaButton = tk.Button(ventana, text="Crear contraseña",fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.contraCrear)
        self.ContraseñaButton.pack(pady=10)

        # Fortaeza de la contraseña label
        self.strength_label = tk.Label(ventana, text="")
        self.strength_label.pack(padx=10, pady=5)
        # Entrada de la contraseña
        self.MostrarCon = tk.StringVar()
        self.ContEnt = tk.Entry(ventana, textvariable=self.MostrarCon, width=30)
        self.ContEnt.pack(padx=10, pady=5)

    def contraCrear(self):
        largo = int(self.largoVar.get())
        Mayusculas = self.MayusVar.get()
        Especial = self.especialVar.get()
        numeross=self.numerosVar.get()

        Generacion = Generador(largo=largo, mayusculas=Mayusculas,
                                            especial=Especial, numero=numeross)

        password = Generacion.CrearContraseña()
        self.MostrarCon.set(password)

        strength = Generacion.verificarContraseña(password)
        self.strength_label.config(text=strength)
        
        messagebox.showinfo("Exito", "La contraseña es: " + password)

ventana = tk.Tk()
gui = PasswordGeneratorGUI(ventana)
ventana.mainloop()