
from producto import Producto
from categoria import Categoria
from usuario import Usuario
from compra import Compra

class SistemaGestionVentas():
    def __init__(self,nombre:str) -> None:
        self.__nombre = nombre
        self.__total_acumulado = 0
        self.__caja_abierta = False
        self.__caja_cerrada = False
        self.__lista_compras = []
        self.__usuarios = []
        self.__productos = []
        self.__categorias = []
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @property
    def total_acumulado(self):
        return self.__total_acumulado
    
    @total_acumulado.setter
    def total_acumulado(self,nuevo_total_acumulado):
        self.__total_acumulado = nuevo_total_acumulado
    
    @property
    def caja_abierta(self):
        return self.__caja_abierta
    
    @caja_abierta.setter
    def caja_abierta(self,nuevo_caja_abierta):
        self.__caja_abierta = nuevo_caja_abierta
    
    @property
    def caja_cerrada(self):
        return self.__caja_cerrada
    
    @caja_cerrada.setter
    def caja_cerrada(self,nuevo_caja_cerrada):
        self.__caja_cerrada = nuevo_caja_cerrada
    
    
    @property
    def lista_compras(self):
        return self.__lista_compras
    
    @lista_compras.setter
    def lista_compras(self,nuevo_lista_compras):
        self.__lista_compras = nuevo_lista_compras
        
    @property
    def usuarios(self):
        return self.__usuarios
    
    @usuarios.setter
    def usuarios(self,nuevo_usuarios):
        self.__usuarios = nuevo_usuarios
        
    @property
    def productos(self):
        return self.__productos
    
    @productos.setter
    def productos(self,nuevo_productos):
        self.__productos = nuevo_productos
    
    @property
    def categorias(self):
        return self.__categorias
    
    @categorias.setter
    def categorias(self,nuevo_categorias):
        self.__categorias = nuevo_categorias
    
    def abrir_caja(self):
        self.__caja_abierta = True
        self.__caja_cerrada = False
        
    def cerrar_caja(self):
        self.__caja_cerrada = True
        self.__caja_abierta = False
        
    def registrar_compra(self,compra:Compra):
        self.__lista_compras.append(compra)
        
    def registrar_usuario(self,usuario:Usuario):
        self.__usuarios.append(usuario)
    
    def eliminar_usuario(self,usuario:Usuario):
        self.__usuarios.remove(usuario)
    
    def agregar_producto(self,producto: Producto):
        self.__productos.append(producto)
    
    def eliminar_producto(self, producto: Producto):
        self.__productos.remove(producto)
        
    def añadir_categoria(self, categoria: Categoria):
        self.__categorias.append(categoria)
    
    def eliminar_categoria(self, categoria: Categoria):
        self.__categorias.remove(categoria)
     
    
    
    def __str__(self):
        return f"Nombre Negocio: {self.nombre}"
    
    


sistemaGestionVentas1 = SistemaGestionVentas("Mercado Ricky Maravilla")



producto1 = Producto("Alfajor Oreo Milka", "Alfajor 100gr Milka ", 850.22,40,"Alfajores")
producto2 = Producto("Alfajor Guaymallen", "-", 850.22,40,"Alfajores")

compra1 = Compra("efectivo")
compra1.agregar_producto(producto1)
compra1.agregar_producto(producto2)
compra1.eliminar_producto(producto1)
compra1.finalizar_compra()

print(compra1)

print(producto1)
    
sistemaGestionVentas1.registrar_compra(compra1)
sistemaGestionVentas1.cerrar_caja()
print(sistemaGestionVentas1.caja_cerrada)
print(sistemaGestionVentas1.caja_abierta)