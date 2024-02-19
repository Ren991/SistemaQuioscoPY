import tkinter as tk

class PantallaCajaSupermercado:
    def __init__(self, root):
        self.root = root
        self.root.title("Caja del Supermercado")
        
        # Configurar el tamaño de la ventana
        self.root.geometry("400x300")  # Ancho x Alto
        
        # Contenido de la ventana de la caja del supermercado
        self.label_titulo = tk.Label(root, text="¡Bienvenido a la Caja del Supermercado!")
        self.label_titulo.pack(pady=10)
        
        # Crear un frame para los botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)
        
        # Botón para nueva compra
        self.button_nueva_compra = tk.Button(self.frame_botones, text="Nueva Compra")
        self.button_nueva_compra.pack(side="left", padx=5)
        
        # Botón para cerrar caja
        self.button_cerrar_caja = tk.Button(self.frame_botones, text="Cerrar Caja")
        self.button_cerrar_caja.pack(side="left", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaCajaSupermercado(root)
    root.mainloop()
    root.mainloop()
