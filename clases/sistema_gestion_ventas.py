class SistemaGestionVentas():
    def __init__(self,nombre:str) -> None:
        self.__nombre = nombre
        self.__total_acumulado = 0
        self.__caja_abierta = False
        self.__caja_cerrada = False
        self.__lista_compras = []
        self.__usuarios = []
        self.__productos = []
        
        
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
    
    def abrir_caja(self):
        self.__caja_abierta = True
        
    def cerrar_caja(self):
        self.__caja_cerrada = True
        self.__caja_abierta = False
        
    def registrar_compra(self):
        pass
    
    
        