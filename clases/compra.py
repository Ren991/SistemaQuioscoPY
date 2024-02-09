from datetime import *


class Compra():
    id_compra = 0
    def __init__(self) -> None:
        Compra.id_compra += 1
        self.__id = Compra.id_compra
        self.__metodo_pago = None
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
        
    
    
    
    
    
    
        
        