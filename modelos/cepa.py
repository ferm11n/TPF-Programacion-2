import json
from EntidadVineria import EntidadVineria


class Cepa(EntidadVineria):

    def __init__(self, id: str, nombre: str):
        super().__init__(id, nombre) 

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)
    
    #Agregamos aca
    def obtenerVinos(self):
        from vinoteca import Vinoteca
        #Usamos el servicio de vinoteca para obtener todos los vinos y filtrar por la cepa
        todosLosVinos = Vinoteca.obtenerVinos(anio=None, orden=None, reverso=None)
        return [vino for vino in todosLosVinos if self.obtenerId() in vino.obtenerCepas()]
    
