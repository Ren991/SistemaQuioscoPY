import tkinter as tk
from sistema_gestion_ventas import SistemaGestionVentas

class PantallaAdministracion:
    def __init__(self, root, username, mercado):
        self.root = root
        self.root.title("Panel de Administración")
        
        
        # Configurar el tamaño de la ventana
        self.root.geometry("400x300")  # Ancho x Alto
        
        # Configuración de la barra de título
        self.label_titulo = tk.Label(root, text="Bienvenido, " + username)
        self.label_subtitulo = tk.Label(root, text="Gestión de =>" + mercado.nombre)
        self.label_titulo.pack(side="top", fill="x")
        self.label_subtitulo.pack(side="top", fill="x")
        
        # Aquí puedes agregar más widgets para administrar el negocio

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAdministracion(root, PantallaAdministracion.username, PantallaAdministracion.mercado.nombre)
    root.mainloop()