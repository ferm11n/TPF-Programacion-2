# librerias
import os
import json

# modelos


class Vinoteca:

    _archivoDeDatos = "vinoteca.json"
    _bodegas = []
    _cepas = []
    _vinos = []

    @classmethod
    def inicializar(cls):
        try:
            datos = cls._parsearArchivoDeDatos()
            cls._convertirJsonAListas(datos)
        except FileNotFoundError:
            raise Exception(f"Error: No esta el archivo {cls._archivoDeDatos}")
        except json.JSONDecodeError:
            raise Exception(f"Error: El archivo JSON esta mal formado")
        except Exception as e:
            raise Exception(f"Error inesperado {e}")

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        """return sorted(cls.bodegas, key=lambda x: getattr(x, orden), reverse=reverso) if orden else cls.bodegas"""
        
        bodegas = cls._bodegas
        if isinstance(orden, str):
            if orden == "nombre":
                bodegas.sort(key=lambda b: b.obtenerNombre())
            elif orden == "vinos":
                bodegas.sort(key=lambda b: len(b.obtenerVinos()))
        if reverso:
            bodegas.reverse()
        return bodegas
    
    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        """return sorted(cls.cepas, key=lambda x: getattr(x, orden), reverse=reverso) if orden else cls.cepas"""        
        
        cepas = cls._cepas
        if isinstance(orden, str):
            if orden == "nombre":
                cepas.sort(key=lambda c: c.obtenerNombre())
        if reverso:
            cepas.reverse()
        return cepas
    
    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        """vinosFiltrados = [vino for vino in cls.vinos if anio in vino.obtenerPartidas()] if anio else cls.vinos 
        return sorted(vinosFiltrados, ley=lambda x: getattr(x, orden), reverse=reverso) if orden else vinosFiltrados"""
        
        vinos = cls._vinos
        if anio is not None:
            vinos = [vino for vino in vinos if vino.obtenerAnio() == anio]
        if isinstance(orden, str):
            if orden == "nombre":
                vinos.sort(key=lambda v: v.obtenerNombre())
            elif orden == "bodega":
                vinos.sort(key=lambda v: v.obtenerBodega().obtenerNombre())
            elif orden == "cepas":
                vinos.sort(key=lambda v: [cepa.obtenerNombre() for cepa in v.obtenerCepas()])
        if reverso:
            vinos.reverse()
        return vinos
    
    @classmethod
    def buscarBodega(cls, id):
        from modelos.bodega import Bodega
        for bodega in cls._bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None
        
    
    @classmethod
    def buscarCepa(cls, id):
        from modelos.cepa import Cepa
        for cepa in cls._cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None
        
    
    @classmethod
    def buscarVino(cls, id):
        from modelos.vino import Vino
        for vino in cls._vinos:
            if vino.obtenerId() == id:
                return vino
        return None
    
    @classmethod
    def _parsearArchivoDeDatos(cls):
        with open(cls._archivoDeDatos, 'r') as archivo:
            data = json.load(archivo)
        return data
    
    @classmethod
    def _convertirJsonAListas(cls, data):
        from modelos.bodega import Bodega
        from modelos.cepa import Cepa
        from modelos.vino import Vino


        #cls._bodegas = [Bodega(**bodega) for bodega in data.get('bodegas', [])]

        cls._cepas = [Cepa(**cepa) for cepa in data.get('cepas', [])]
        cls._vinos = [Vino(**vino) for vino in data.get('vinos', [])]

        cls._bodegas = []
        for bodega in data.get('bodegas', []):
            bodegaObj = Bodega(**bodega)

            #Verificamos si cepas esta en el dicc
            if 'cepas' in bodega:
                bodegaObj.cepas = [cls.buscarCepa(cepaId) for cepaId in bodega['cepas']]
            else:
                bodegaObj.cepas = [] #Asignamos lista vacia si no existe
            
            #Verifcamos si vinos esta en el diccionario
            if 'vinos' in bodega:
                bodegaObj.vinos = [cls.buscarVino(vinoId) for vinoId in bodega['vinos']]
            else:
                bodegaObj.vinos = [] #Asignamos la lista vacia si no existe

            cls._bodegas.append(bodegaObj)

            #print("Datos cargados: ", data)

        #Testeos
        """print(f"Bodegas cargas: {cls._bodegas}")
        print(f"Cepas cargadas: {cls._cepas}")
        print(f"Vinos cargados: {cls._vinos}")"""

#Aca inicializamos la vinoteca
Vinoteca.inicializar()
#print(Vinoteca._bodegas)
        
