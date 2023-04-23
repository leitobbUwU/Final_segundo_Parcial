class Login:
    def __init__(self, user, contraseña):
            self.usuario = user
            self.contraseña = contraseña

    def login(self):
        if self.usuario == "Usuario" and self.contraseña == "Admin":
            return True
        else:
            return False