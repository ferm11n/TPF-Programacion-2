import json
from EntidadVineria import EntidadVineria
#from vinoteca import Vinoteca

class Vino(EntidadVineria):

    def __init__(self, id: str, nombre: str, bodega: str, cepas: list, partidas: list):
        super().__init__(id, nombre) #Llamamos al constructor de la clase base
        self.bodega = bodega
        self.cepas = cepas
        self.partidas = partidas

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodegas().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodegas().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
    

    #Agregamos esto
    def obtenerBodegas(self):
        from vinoteca import Vinoteca
        return Vinoteca.buscarBodega(self.bodega) #Con esto buscamos la bodega que esta asociada al vino
    
    def obtenerCepas(self):
        from vinoteca import Vinoteca
        #Usa el servicio de Vinoteca para obtener todas las cepas y filtrar por las cepas
        todasLasCepas = Vinoteca.obtenerCepas(orden=None, reverso=None)
        return [cepa for cepa in todasLasCepas if cepa.obtenerId() in self.cepas]
    
    def obtenerPartidas(self) -> list:
        return self._partidas
    
    #Hasta aca
