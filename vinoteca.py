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
        datos = Vinoteca._parsearArchivoDeDatos()
        Vinoteca._convertirJsonAListas(datos)

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
        cls.bodegas = [Bodega(**bodega) for bodega in data['bodegas']]
        cls.cepas = [Cepa(**cepa) for cepa in data['cepas']]
        cls.vinos = [Vino(**vino) for vino in data['vinos']]

#Aca inicializamos la vinoteca
Vinoteca.inicializar()
#print(Vinoteca._bodegas)
        
