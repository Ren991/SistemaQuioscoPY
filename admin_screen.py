import tkinter as tk
from tkinter import ttk
from datos import productos

class PantallaAdministracion:
    def __init__(self, root, username, mercado):
        self.root = root
        self.root.title("Panel de Administración")
        
        # Configurar el tamaño de la ventana
        self.root.geometry("800x400")  # Ancho x Alto
        
        # Configuración de la barra de título
        self.label_titulo = tk.Label(root, text="Bienvenido, " + username)
        self.label_titulo.pack(side="top", fill="x")
        self.label_subtitulo = tk.Label(root, text="Gestión de =>" + mercado.nombre)
        self.label_subtitulo.pack(side="top", fill="x")
        
        # Botón para ver productos
        self.button_ver_productos = tk.Button(root, text="Ver Productos", command=self.ver_productos)
        self.button_ver_productos.pack(pady=10)
        
        # Botón para cerrar la tabla (inicialmente oculto)
        self.button_cerrar_tabla = tk.Button(root, text="Cerrar Tabla", command=self.cerrar_tabla, state=tk.DISABLED)
        self.button_cerrar_tabla.pack(pady=5)
        
        # Variable para almacenar la tabla
        self.tree = None
    
    def ver_productos(self):
        # Verificar si la tabla ya está creada y mostrada
        if self.tree is not None:
            return
        
        # Crear la tabla
        self.tree = ttk.Treeview(self.root, columns=("Nombre", "Descripción", "Precio", "Stock", "Categoría"))
        
        # Configurar las columnas (código de columnas y encabezados de columnas aquí)
        self.tree.heading("#0", text="ID")
        self.tree.heading("Nombre", text="Nombre", anchor="center")
        self.tree.heading("Descripción", text="Descripción", anchor="center")
        self.tree.heading("Precio", text="Precio", anchor="center")
        self.tree.heading("Stock", text="Stock", anchor="center")
        self.tree.heading("Categoría", text="Categoría", anchor="center")
        
        # Insertar los productos en la tabla
        for producto in productos:
            self.tree.insert("", 0, text=producto.id, values=(producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria.nombre))
        
        # Empaquetar la tabla en la ventana
        self.tree.pack(expand=True, fill=tk.BOTH)
        
        # Habilitar el botón para cerrar la tabla
        self.button_cerrar_tabla.config(state=tk.NORMAL)
    
    def cerrar_tabla(self):
        # Verificar si la tabla existe
        if self.tree is not None:
            # Destruir la tabla
            self.tree.destroy()
            self.tree = None
        
        # Deshabilitar el botón para cerrar la tabla
        self.button_cerrar_tabla.config(state=tk.DISABLED)
if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAdministracion(root, PantallaAdministracion.username, PantallaAdministracion.mercado.nombre)
    root.mainloop()