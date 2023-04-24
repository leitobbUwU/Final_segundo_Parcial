import tkinter as tk
from tkinter import messagebox
from LogicaRomano import Numeros

class Convertidor:
    def __init__(self, ventana):
        self.window = ventana
        ventana.title("Conversor Romano a decimal")
        ventana.geometry("800x600")

        self.label1 = tk.Label(ventana, font=("Helvetica",15), text="Ingrese un número romano entre 1 y 50:")
        self.label1.pack(padx=10, pady=5, fill=tk.X)

        self.numero1 = tk.Entry(ventana, font=("Helvetica",30))
        self.numero1.pack(padx=10, pady=5, fill=tk.X)

        self.botonCon1 = tk.Button(ventana, text="Convertir Romano a Decimal", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.RomanoDecimal)
        self.botonCon1.pack(padx=10, pady=5, fill=tk.X)

        self.label2 = tk.Label(ventana, font=("Helvetica",15), text="Ingrese un número decimal entre 1 y 50:")
        self.label2.pack(padx=10, pady=5, fill=tk.X)

        self.numero2 = tk.Entry(ventana, font=("Helvetica",30))
        self.numero2.pack(padx=10, pady=5, fill=tk.X)

        self.botonCon2 = tk.Button(ventana, text="Convertir Decimal a Romano", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.DecimalRomano)
        self.botonCon2.pack(padx=10, pady=5, fill=tk.X)

        self.resultado = tk.StringVar()
        self.label3 = tk.Label(ventana, font=("Helvetica",30), textvariable=self.resultado)
        self.label3.pack(padx=10, pady=5, fill=tk.X)

    def RomanoDecimal(self):
        valor = self.numero1.get()

        # Validar que el valor ingresado es un número romano válido
        if not valor.isalpha():
            self.resultado.set("Ingrese un número romano válido")
            return

        roman_converter = Numeros()
        
        # Validar que el número romano se encuentra en el rango de 1 a 50
        if roman_converter.RomanoArabigo(valor) < 1 or roman_converter.RomanoArabigo(valor) > 50:
            self.resultado.set("Ingrese un número romano válido entre 1 y 50")
            return

        resultado = roman_converter.RomanoArabigo(valor)

        messagebox.showinfo("Numero Decimal", resultado)

    def DecimalRomano(self):
        valor = self.numero2.get()

        # Validar que el valor ingresado es un número decimal válido
        if not valor.isnumeric() or int(valor) < 1 or int(valor) > 50:
            self.resultado.set("Ingrese un número decimal válido entre 1 y 50")
            return

        roman_converter = Numeros()

        resultado = roman_converter.ArabigoRomano(int(valor))

        messagebox.showinfo("Numero Romano", resultado)

ventana = tk.Tk()
w = Convertidor(ventana)
ventana.mainloop()
