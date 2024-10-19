#Importaciones
from abc import ABC, abstractmethod



#Clase abstracta EntidadVineria
class EntidadVineria(ABC):
    def __init__(self, id: str, nombre: str):
        self._id = id
        self._nombre = nombre


    def establecerNombre(self, nombre: str):
        self._nombre = nombre

    def obtenerId(self) -> str:
        return self._id
    
    def obtenerNombre(self) -> str:
        return self._nombre
    
    @abstractmethod
    def convertirAJSON(self) -> dict:
        pass

    def __eq__(self, other):
        if isinstance(other, EntidadVineria):
            return self._id == other._id
        return False
#Finish