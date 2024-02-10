class Categoria():
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def __str__(self) -> str:
        return f"Categoria : {self.nombre}"
    

categoria1 = Categoria("Golosinas")
print(categoria1)
        