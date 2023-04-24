from tkinter import messagebox


class Numeros:
    def __init__(self):
        self.romanos = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XLIX": 49,
            "XLVIII": 48,
            "XLVII": 47,
            "XLVI": 46,
            "XLV": 45,
            "XLIV": 44,
            "XLIII": 43,
            "XLII": 42,
            "XLI": 41,
        }

        self.arabigos = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            45: "XLV",
            46: "XLVI",
            47: "XLVII",
            48: "XLVIII",
            49: "XLIX",
            50: "L",
        }


    def ArabigoRomano(self, numero):
        resultado = ""

        for arabigo, romano in sorted(self.arabigos.items(), reverse=True):
            while numero >= arabigo:
                resultado += romano
                numero -= arabigo

        return resultado

    def RomanoArabigo(self, numero):
        resultado = 0
        i = 0

        while i < len(numero):
            if i + 1 < len(numero) and self.romanos[numero[i]] < self.romanos[numero[i+1]]:
                resultado += self.romanos[numero[i+1]] - self.romanos[numero[i]]
                i += 2
            else:
                resultado += self.romanos[numero[i]]
                i += 1
        
        # Verificar si el número romano es válido
        for j in range(len(numero)-1):
            if self.romanos[numero[j]] < self.romanos[numero[j+1]]:
                messagebox.showerror("Error", "El número romano ingresado es inválido.")
                return None

        return resultado
