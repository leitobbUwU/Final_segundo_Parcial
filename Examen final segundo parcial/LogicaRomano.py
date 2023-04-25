from tkinter import messagebox


class Numeros:
    def __init__(self):
        self.romanos = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9,
            "X": 10,
            "XI": 11,
            "XII": 12,
            "XIII": 13,
            "XIV": 14,
            "XV": 15,
            "XVI": 16,
            "XVII": 17,
            "XVIII": 18,
            "XIX": 19,
            "XX": 20,
            "XXI": 21,
            "XXII": 22,
            "XXIII": 23,
            "XXIV": 24,
            "XXV": 25,
            "XXVI": 26,
            "XXVII": 27,
            "XXVIII": 28,
            "XXIX": 29,
            "XXX": 30,
            "XXXI": 31,
            "XXXII": 32,
            "XXXIII": 33,
            "XXXIV": 34,
            "XXXV": 35,
            "XXXVI": 36,
            "XXXVII": 37,
            "XXXVIII": 38,
            "XXXIX": 39,
            "XL": 40,
            "XLI": 41,
            "XLII": 42,
            "XLIII": 43,
            "XLIV": 44,
            "XLV": 45,
            "XLVI": 46,
            "XLVII": 47,
            "XLVIII": 48,
            "XLIX": 49,
            "L": 50
        }

        self.arabigos = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            11: "XI",
            12: "XII",
            13: "XIII",
            14: "XIV",
            15: "XV",
            16: "XVI",
            17: "XVII",
            18: "XVIII",
            19: "XIX",
            20: "XX",
            21: "XXI",
            22: "XXII",
            23: "XXIII",
            24: "XXIV",
            25: "XXV",
            26: "XXVI",
            27: "XXVII",
            28: "XXVIII",
            29: "XXIX",
            30: "XXX",
            31: "XXXI",
            32: "XXXII",
            33: "XXXIII",
            34: "XXXIV",
            35: "XXXV",
            36: "XXXVI",
            37: "XXXVII",
            38: "XXXVIII",
            39: "XXXIX",
            40: "XL",
            41: "XLI",
            42: "XLII",
            43: "XLIII",
            44: "XLIV",
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
        if not self.validar_romano(numero):
            return None
        
        resultado = 0
        i = 0

        while i < len(numero):
            if i + 1 < len(numero) and self.romanos[numero[i]] < self.romanos[numero[i+1]]:
                resultado += self.romanos[numero[i+1]] - self.romanos[numero[i]]
                i += 2
            else:
                resultado += self.romanos[numero[i]]
                i += 1

        return resultado
    
    def validar_romano(self, numero):
        # Verificar que los símbolos de resta se utilicen correctamente
        if "IL" in numero or "IC" in numero or "ID" in numero or "IM" in numero or \
            "VX" in numero or "VL" in numero or "VC" in numero or "VD" in numero or "VM" in numero or \
            "XD" in numero or "XM" in numero:
            messagebox.showerror("Error", "El número romano ingresado es inválido.")
            return False
        
        # Verificar que no se utilicen más de 3 letras consecutivas iguales
        for simbolo in ["I", "X", "C", "M"]:
            if numero.count(simbolo*4) > 0:
                messagebox.showerror("Error", "El número romano ingresado es inválido.")
                return False
            
        # Verificar que no se utilicen más de una letra de resta consecutivamente
        if "IV" in numero or "IX" in numero or "XL" in numero or \
            "XC" in numero or "CD" in numero or "CM" in numero:
            messagebox.showerror("Error", "El número romano ingresado es inválido.")
            return False
        
        return True
    
