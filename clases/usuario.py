import random

class Usuario:
    ids_generados = []

    def __init__(self, nombre: str, contraseña: str, rol: str) -> None:
        self.__nombre = nombre
        self.__contraseña = contraseña
        self.__rol = rol
        self.__id = self.generar_id()
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id
    
    
    @property
    def contraseña(self):
        return self.__contraseña
    
    @contraseña.setter
    def contraseña(self, nuevo_contraseña):
        self.__contraseña = nuevo_contraseña
    
    @property
    def rol(self):
        return self.__rol
    
    @rol.setter
    def rol(self, nuevo_rol):
        self.__rol = nuevo_rol
    
    def __str__(self) -> str:
        return f"ID : {self.id} // Nombre : {self.nombre} // Contraseña : {self.contraseña} // Rol : {self.rol} "
    
    def generar_id(self) -> str:
        while True:
            nuevo_id = ''.join(random.choices('0123456789', k=5))
            if nuevo_id not in Usuario.ids_generados:
                Usuario.ids_generados.append(nuevo_id)
                return nuevo_id
        
        
        
prueba_usuario1 = Usuario("Pepe","1234", "Administrador")
print(prueba_usuario1)