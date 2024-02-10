import tkinter as tk

class PantallaAdministracion:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Administración")
        
        self.label_bienvenida = tk.Label(root, text="¡Bienvenido al Panel de Administración!")
        self.label_bienvenida.pack()
        
        # Aquí puedes agregar más widgets para administrar el negocio

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAdministracion(root)
    root.mainloop()