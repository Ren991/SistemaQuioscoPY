class Producto():
    id_producto = 0
    def __init__(self, nombre:str, descripcion:str,precio:float,stock:int, categoria: str) -> None:
        Producto.id_producto += 1
        self.__id = Producto.id_producto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
        self.__categoria = categoria
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, nuevo_descripcion):
        self.__descripcion = nuevo_descripcion
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio
    
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, nuevo_categoria):
        self.__categoria = nuevo_categoria
        
    def __str__(self) -> str:
        return f"Id Producto: {self.id} | Nombre Producto: {self.nombre} | Descripcion: {self.descripcion} | Precio: {self.precio} | Stock: {self.stock} | Categoria : {self.categoria}"
    

producto1 = Producto("Alfajor Oreo Milka", "Alfajor 100gr Milka ", 850.22,40)
print(producto1)

producto2 = Producto("Alfajor Guaymallen", "-", 850.22,40)
print(producto2)

