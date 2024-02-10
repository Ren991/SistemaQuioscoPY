from datetime import *
from producto import Producto


class Compra():
    id_compra = 0
    def __init__(self, metodo_pago:str) -> None:
        Compra.id_compra += 1
        self.__id = Compra.id_compra
        self.__metodo_pago = metodo_pago
        self.__productos = []
        self.__total = 0
        self.__fecha = datetime.today()
        self.__status_compra = False # False == Compra no abonada. True == Compra abonada
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,nuevo_id):
        self.__id = nuevo_id
    
    @property
    def metodo_pago(self):
        return self.__metodo_pago
    
    @metodo_pago.setter
    def metodo_pago(self,nuevo_metodo_pago):
        self.__metodo_pago = nuevo_metodo_pago
    
    @property
    def productos(self):
        return self.__productos
    
    @productos.setter
    def productos(self,nuevo_productos):
        self.__productos = nuevo_productos

    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self,nuevo_total):
        self.__total = nuevo_total
    
    @property
    def fecha(self):
        return f"{self.__fecha.day}/{self.__fecha.month}/{self.__fecha.year}"
    
    @property
    def status_compra(self):
        return self.__status_compra
    
    @status_compra.setter
    def status_compra(self,nuevo_status_compra):
        self.__status_compra = nuevo_status_compra
        
    def __str__(self) -> str:
        productos_str = ", ".join(str(producto) for producto in self.productos)
        return f"ID de compra: {self.id} |||| Productos: {productos_str} |||| Total: {self.total} || Fecha: {self.fecha}"
        
    
    def finalizar_compra(self):
        self.__status_compra = True
    
    def agregar_producto(self,producto: Producto):
        self.__productos.append(producto)
        self.__total += producto.precio
        producto.stock -= 1
        
        
    def eliminar_producto(self, producto: Producto):
        self.__productos.remove(producto)
        producto.stock += 1
  
    
    
    
    
producto1 = Producto("Alfajor Oreo Milka", "Alfajor 100gr Milka ", 850.22,40,"Alfajores")
producto2 = Producto("Alfajor Guaymallen", "-", 850.22,40,"Alfajores")

compra1 = Compra("efectivo")
compra1.agregar_producto(producto1)
compra1.agregar_producto(producto2)
compra1.eliminar_producto(producto1)
compra1.finalizar_compra()

#print(compra1)

print(producto1)