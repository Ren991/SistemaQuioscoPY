import tkinter as tk
from tkinter import messagebox
from admin_screen import PantallaAdministracion
from datos import *

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        
        # Configurar el tamaño de la ventana
        self.root.geometry("400x300")  # Ancho x Alto
        
        self.label_username = tk.Label(root, text="Usuario:")
        self.label_username.pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()
        
        self.label_password = tk.Label(root, text="Contraseña:")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(root, text="Iniciar Sesión", command=self.login)
        self.button_login.pack()
    
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        mercado = sistemaGestionVentas1
        # Verificar las credenciales ingresadas con los usuarios existentes
        for usuario in usuarios:
            if usuario.nombre == username and usuario.contraseña == password:
                messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
                # Abrir la pantalla de administración después del inicio de sesión exitoso
                self.root.destroy()  # Cerrar la pantalla de inicio de sesión
                root_admin = tk.Tk()
                app_admin = PantallaAdministracion(root_admin, username, mercado)
                root_admin.mainloop()
                return
        
        # Si las credenciales no coinciden con ningún usuario existente
        messagebox.showerror("Inicio de Sesión", "Usuario o contraseña incorrectos")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()
