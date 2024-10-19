import json
from EntidadVineria import EntidadVineria
from vinoteca import Vinoteca


class Bodega(EntidadVineria):

    def __init__(self, id: str, nombre: str):
        super().__init__(id, nombre) #Esto es para llamar al constructor de la clase base
        self._vinos = [] #Inicializamos con una lista vacia

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)
    
    
    #---------------> Agregamos ObtenerVinos y ObtenerCepas <-----------------
    def obtenerVinos(self):
        #Usamos un servicio de vinoteca para poder asi obtener los vinos y filtrar por la bodega
        todosLosVinos = Vinoteca.obtenerVinos(anio=None, orden=None, reverso=None)
        return [vino for vino in todosLosVinos  if vino.obtenerBodegas().obtenerId() == self.obtenerId]
    

    def obtenerCepas(self):
        #Usamos el servicio de vinoteca para obtener todas las cepas que esten asociadas a la bodega
        vinosDeLaBodega = self.obtenerVinos()
        cepasSet = set() #Esto es para setear y evitar duplicados
        for vino in vinosDeLaBodega:
            cepas = vino.obtenerCepas()
            cepasSet.update(cepas) #Aca agregamos las cepas del vino al set
        return list(cepasSet)
    #---------------> Hasta aca <-----------------