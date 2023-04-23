import random

class Generador:
    def __init__(self, largo=8, mayusculas=True, especial=True, numero =True):
        self.largo = largo
        self.Mayusculas = mayusculas
        self.Especiales = especial
        self.Numero = numero

        self.letras = "abcdefghijklmnopqrstuvwxyz"
        self.Mayusculass = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numeros = "0123456789"
        self.Especialess = "!#$%&()*+,-./:;<=>?@[\]^_{|}~"

    def CrearContraseña(self):
        contraseña = self.letras

        if self.Mayusculas:
            contraseña += self.Mayusculass

        if self.Especiales:
            contraseña += self.Especialess
            
        if self.Numero:
            contraseña  +=self.numeros

        password = "".join(random.choices(contraseña, k=self.largo))
        return password

    def verificarContraseña(self, contraseña):
        CuentaMayus = 0
        CuentaNum = 0
        CuentaEsp = 0

        for caracteres in contraseña:
            if caracteres in self.Mayusculass:
                CuentaMayus += 1
            elif caracteres in self.numeros:
                CuentaNum += 1
            elif caracteres in self.Especialess:
                CuentaEsp += 1

        if self.Mayusculas and CuentaMayus == 0:
            return "Debil - Incluir letras mayúsculas"
        elif self.Especiales and CuentaEsp == 0:
            return "Débil - Incluir caracteres especiales"
        elif self.numeros and CuentaNum == 0:
            return "Débil - Incluir Numeros"
        elif len(contraseña) < 8:
            return "Débil: la contraseña debe tener al menos 8 caracteres"
        elif len(contraseña) >= 8 and CuentaNum > 0 and CuentaMayus > 0 and CuentaEsp > 0:
            return "Fuerte"
        else:
            return "Moderada"