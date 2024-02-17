import tkinter as tk
from tkinter import ttk
from datos import productos, Producto, Categoria
from datetime import datetime
from tkinter.simpledialog import askstring

class PantallaAdministracion:
    def __init__(self, root, username, mercado):
        self.root = root
        self.root.title("Panel de Administración")
        
        # Configurar el tamaño de la ventana
        self.root.geometry("800x400")  # Ancho x Alto
        
        # Configurar la fecha y hora actual
        self.fecha_hora_actual = tk.StringVar()
        self.actualizar_fecha_hora()  # Actualizar fecha y hora inicialmente
        
        # Configuración de la barra de título
        self.label_fecha_hora = tk.Label(root, textvariable=self.fecha_hora_actual, font=("Arial", 10), fg="blue")
        self.label_fecha_hora.pack(side="top", fill="x")  # Colocar en la esquina superior derecha
        self.label_titulo = tk.Label(root, text="Bienvenido, " + username)
        self.label_titulo.pack(side="top", fill="x")
        self.label_subtitulo = tk.Label(root, text="Gestión de =>" + mercado.nombre)
        self.label_subtitulo.pack(side="top", fill="x")
        
        # Botón para ver productos
        self.button_ver_productos = tk.Button(root, text="Ver Productos", command=self.ver_productos)
        self.button_ver_productos.pack(pady=10)
        
        # Botón para agregar productos
        self.button_agregar_producto = tk.Button(root, text="Agregar Producto", command=self.agregar_producto)
        self.button_agregar_producto.pack(pady=5)
        
        # Botón para cerrar la tabla (inicialmente oculto)
        self.button_cerrar_tabla = tk.Button(root, text="Cerrar Tabla", command=self.cerrar_tabla, state=tk.DISABLED)
        self.button_cerrar_tabla.pack(pady=5)

        # Botón para abrir la caja
        self.button_abrir_caja = tk.Button(root, text="Abrir caja", command= self.abrir_caja)
        self.button_abrir_caja.pack(pady=10)
        # Variable para almacenar la tabla
        self.tree = None
        
        self.actualizar_fecha_hora_continuamente()
        
    def abrir_caja(self):
        print("Abriendo caja")

    def actualizar_fecha_hora(self):
        now = datetime.now()
        self.fecha_hora_actual.set(now.strftime("%Y-%m-%d %H:%M:%S"))
    
    def actualizar_fecha_hora_continuamente(self):
        self.actualizar_fecha_hora()  # Actualizar la fecha y hora
        self.root.after(1000, self.actualizar_fecha_hora_continuamente)
    
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
        
        # Configurar el menú contextual para eliminar productos
        self.menu_contextual = tk.Menu(self.root, tearoff=0)
        self.menu_contextual.add_command(label="Eliminar Producto", command=self.eliminar_producto)
        self.menu_contextual.add_command(label="Editar Producto", command=self.editar_producto) 
        self.tree.bind("<Button-3>", self.mostrar_menu_contextual)

    
    def cerrar_tabla(self):
        # Verificar si la tabla existe
        if self.tree is not None:
            # Destruir la tabla
            self.tree.destroy()
            self.tree = None
        
        # Deshabilitar el botón para cerrar la tabla
        self.button_cerrar_tabla.config(state=tk.DISABLED)
        
    def agregar_producto(self):
        # Solicitar al usuario los detalles del nuevo producto
        nombre = askstring("Agregar Producto", "Nombre del Producto:")
        descripcion = askstring("Agregar Producto", "Descripción:")
        precio = float(askstring("Agregar Producto", "Precio:"))
        stock = int(askstring("Agregar Producto", "Stock:"))
        categoria = askstring("Agregar Producto", "Categoría:")
        
        # Crear una instancia del objeto Producto
        nuevo_producto = Producto(nombre, descripcion, precio, stock, Categoria(categoria))
        
        # Agregar el nuevo producto al array productos en datos.py
        productos.append(nuevo_producto)
        
        # Actualizar la tabla de productos
        self.ver_productos()
    
    def mostrar_menu_contextual(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.menu_contextual.post(event.x_root, event.y_root)

    def eliminar_producto(self):
        item = self.tree.selection()[0]
        id_producto = self.tree.item(item, "text")
        for producto in productos:
            if producto.id == id_producto:
                productos.remove(producto)
                break
        self.tree.delete(item)

    def editar_producto(self):
        # Obtener el índice del producto seleccionado
        item = self.tree.selection()[0]
        id_producto = self.tree.item(item, "text")

        # Obtener los detalles del producto seleccionado
        nombre = self.tree.item(item, "values")[0]
        descripcion = self.tree.item(item, "values")[1]
        precio = self.tree.item(item, "values")[2]
        stock = self.tree.item(item, "values")[3]
        categoria = self.tree.item(item, "values")[4]

        # Abrir una ventana de diálogo para que el usuario ingrese los nuevos detalles del producto
        nuevo_nombre = askstring("Editar Producto", "Nuevo Nombre del Producto:", initialvalue=nombre)
        nueva_descripcion = askstring("Editar Producto", "Nueva Descripción:", initialvalue=descripcion)
        nuevo_precio = float(askstring("Editar Producto", "Nuevo Precio:", initialvalue=precio))
        nuevo_stock = int(askstring("Editar Producto", "Nuevo Stock:", initialvalue=stock))
        nueva_categoria = askstring("Editar Producto", "Nueva Categoría:", initialvalue=categoria)

        # Actualizar el producto en la lista de productos
        for producto in productos:
            if producto.id == id_producto:
                producto.nombre = nuevo_nombre
                producto.descripcion = nueva_descripcion
                producto.precio = nuevo_precio
                producto.stock = nuevo_stock
                producto.categoria = Categoria(nueva_categoria)
                break

        # Actualizar la tabla de productos
        self.actualizar_tabla_productos()

    def actualizar_tabla_productos(self):
        # Limpiar la tabla actual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar los productos actualizados en la tabla
        for producto in productos:
            self.tree.insert("", 0, text=producto.id, values=(producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria.nombre))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaAdministracion(root, "Usuario", Categoria("Mercado"))
    root.mainloop()
