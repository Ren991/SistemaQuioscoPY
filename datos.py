from sistema_gestion_ventas import SistemaGestionVentas
from categoria import Categoria
from compra import Compra
from producto import Producto
from usuario import Usuario


# INSTANCIA CLASE SISTEMAGESTIONVENTAS

sistemaGestionVentas1 = SistemaGestionVentas("Mercado 1")



# INSTANCIAS CLASE USUARIO
usuarios = []
for i in range(5):
    nombre = "Usuario" + str(i+1)
    contraseña = "password" + str(i+1)
    rol = "Admin" if (i+1) % 2 == 0 else "Vendedor"
    usuario = Usuario(nombre, contraseña, rol)
    usuarios.append(usuario)

# Imprimir las instancias creadas
for usuario in usuarios:
    print(usuario)
    sistemaGestionVentas1.registrar_usuario(usuario)
    
#INSTANCIAS CLASE CATEGORIA

categoria1 = Categoria("Golosinas")
categoria2 = Categoria("Bebidas")
categoria3 = Categoria("Snacks")
categoria4 = Categoria("Frutas")
categoria5 = Categoria("Verduras")
categoria6 = Categoria("Lácteos")
categoria7 = Categoria("Panadería")

# INSTANCIAS CLASE PRODUCTO
productos = []
producto1 = Producto("Chocolate amargo", "Tableta de chocolate con un alto contenido de cacao", 3.50, 100, categoria1)
producto2 = Producto("Agua mineral", "Botella de agua mineral natural sin gas", 1.20, 200, categoria2)
producto3 = Producto("Papas fritas", "Bolsa de papas fritas crujientes y saladas", 2.80, 150, categoria3)
producto4 = Producto("Manzanas", "Manzanas frescas y jugosas", 0.75, 50, categoria4)
producto5 = Producto("Zanahorias", "Zanahorias frescas y crujientes", 0.50, 80, categoria5)
producto6 = Producto("Leche descremada", "Botella de leche descremada pasteurizada", 1.80, 120, categoria6)
producto7 = Producto("Pan integral", "Pan integral recién horneado", 2.00, 90, categoria7)
producto8 = Producto("Helado de vainilla", "Helado cremoso de vainilla con trozos de chocolate", 4.50, 50, categoria1)
producto9 = Producto("Refresco de cola", "Lata de refresco de cola con gas", 1.30, 100, categoria2)
producto10 = Producto("Palitos de queso", "Snack de palitos de queso horneados", 2.20, 80, categoria3)
producto11 = Producto("Naranjas", "Naranjas frescas y jugosas", 0.80, 60, categoria4)
producto12 = Producto("Brócoli", "Brócoli fresco y crujiente", 1.20, 70, categoria5)
producto13 = Producto("Yogur natural", "Envase de yogur natural sin azúcar", 1.00, 110, categoria6)
producto14 = Producto("Pan francés", "Pan francés crujiente recién horneado", 1.50, 120, categoria7)
producto15 = Producto("Barra de chocolate", "Barra de chocolate con leche y nueces", 2.75, 80, categoria1)

productos.extend([producto1, producto2, producto3, producto4, producto5, producto6, producto7, producto8, producto9, producto10, producto11, producto12, producto13, producto14, producto15])

for producto in productos:
    print(producto)
    sistemaGestionVentas1.agregar_producto(producto)
    


    


