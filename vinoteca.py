# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    @classmethod
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    @classmethod
    def obtenerBodegas(orden=None, reverso=False):
        bodegas = cls.__bodegas
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "vinos":
                pass  # completar
        pass  # completar
    
    @classmethod
    def obtenerCepas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
        pass  # completar
    
    @classmethod
    def obtenerVinos(anio=None, orden=None, reverso=False):
        if isinstance(anio, int):
            pass  # completar
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "bodega":
                pass  # completar
            elif orden == "cepas":
                pass  # completar
        pass  # completar
    
    @classmethod
    def buscarBodega(id):
        pass  # completar
    
    @classmethod
    def buscarCepa(id):
        pass  # completar
    
    @classmethod
    def buscarVino(id):
        pass  # completar
    
    @classmethod
    def __parsearArchivoDeDatos():
        pass  # completar
    
    @classmethod
    def __convertirJsonAListas(lista):
        pass  # completar
