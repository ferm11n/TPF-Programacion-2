from flask_restful import Resource
from flask import request
import json
import vinoteca
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class RecursoBodega(Resource):#Mod

    def get(self, id):
        bodega = vinoteca.Vinoteca.buscarBodega(id)
        if isinstance(bodega, Bodega):
            return bodega.convertirAJSONFull(), 200
        return {"error": "Bodega no encontrada"}, 404


class RecursoBodegas(Resource):#mod

    def get(self):
        orden = request.args.get("orden")
        reverso = request.args.get("reverso") == "si" if request.args.get("reverso") else False
        bodegas = vinoteca.Vinoteca.obtenerBodegas(orden=orden, reverso=reverso)
        return [bodega.convertirAJSON() for bodega in bodegas], 200
       


class RecursoCepa(Resource):#mod

    def get(self, id):
        cepa = vinoteca.Vinoteca.buscarCepa(id)
        if isinstance(cepa, Cepa):
            return cepa.convertirAJSONFull(), 200
        return {"error": "Cepa no encontrada"}, 404


class RecursoCepas(Resource):#mod

    def get(self):
        orden = request.args.get("orden")
        reverso = request.args.get("reverso") == "si" if request.args.get("reverso") else False
        cepas = vinoteca.Vinoteca.obtenerCepas(orden=orden, reverso=reverso)
        return [cepa.convertAJSON() for cepa in cepas], 200


class RecursoVino(Resource):#mod

    def get(self, id):
        vino = vinoteca.Vinoteca.buscarVino(id)
        if isinstance(vino, Vino):
            return vino.convertirAJSONFull(), 200
        return {"error": "Vino no encontrado"}, 404


class RecursoVinos(Resource):#mod

    def get(self):
        anio = request.args.get("anio", type=int)
        orden = request.args.get("orden")
        reverso = request.args.get("reverso") == "si" if request.args.get("reverso") else False
        vinos = vinoteca.Vinoteca.obtenerVinos(anio=anio, orden=orden, reverso=reverso)
        return [vino.convertirAJSON() for vino in vinos], 200

