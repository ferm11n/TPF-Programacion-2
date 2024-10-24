from flask import Flask, Response, jsonify, request
import json

app = Flask(__name__)

#Cargamos los datos desde el archivo JSON
with open('vinoteca.json') as f:
    data = json.load(f)

#SEGUNDA PARTE DEL TP
#EJERCICIO 1
@app.route('/api/bodegas/<string:bodega_id>', methods=['GET'])
def getBodega(bodega_id):
    bodega = next((b for b in data['bodegas'] if b['id'] == bodega_id), None)

    if not bodega:
        return jsonify({'error': 'Bodega no encontrada'}), 404
    
    #Obtenemos los vinos que pertenecen a la bodega
    vinosDeBodega = [v for v in data['vinos'] if v['bodega'] == bodega_id]

    #Obtenemos las cepas de los vinos
    cepas_ids = set()
    for vino in vinosDeBodega:
        cepas_ids.update(vino['cepas'])

    #convertir ids de cepas a nombres
    cepasNombres = [c['nombre'] for c in data['cepas'] if c['id'] in cepas_ids]

    #construir el resultado
    result = [
        'id', bodega['id'],
        'nombre', bodega['nombre'],
        'cepas', cepasNombres,
        'vinos', [v['nombre'] for v in vinosDeBodega]
    ]

    #Convertimos el resultado en un orden especifico
    jsonResult = json.dumps(result, ensure_ascii=False)

    return Response(jsonResult, mimetype='application/json')


#EJERCICIO 2
@app.route('/api/cepas/<string:cepa_id>', methods=['GET'])
def getCepa(cepa_id):
    #Buscar la cepa por id
    cepa = next((c for c in data['cepas'] if c['id'] == cepa_id), None)

    if not cepa:
        return jsonify({'error': 'cepa no encontrada'}), 404
    
    #Obtener vinos que pertenecen a la cepa
    vinosDeCepa = [v['nombre'] + " (" + next(b['nombre'] for b in data['bodegas'] if b['id'] == v['bodega']) + ") " for v in data['vinos'] if cepa_id in v['cepas']]

    #Construir el resultado
    result = {
        'id': cepa['id'],
        'nombre': cepa['nombre'],
        'vinos': vinosDeCepa
    }

    jsonResult = json.dumps(result, ensure_ascii=False)
    return Response(jsonResult, mimetype='application/json')


#EJERCICIO 3
@app.route('/api/vinos/<string:vino_id>', methods=['GET'])
def getVino(vino_id):
    #Buscar la cepa por id
    vino = next((v for v in data['vinos'] if v['id'] == vino_id), None)

    if not vino:
        return jsonify({'error': 'vino no encontrado'}), 404
    
    #Obtener la bodega a la que pertenecen el vino
    bodega = next((b['nombre'] for b in data['bodegas'] if b['id'] == vino['bodega']), 'bodega desconocida')

    #Obtener las cepas del vino
    cepasNombre = [c['nombre'] for c in data['cepas'] if c['id'] in vino['cepas']]

    #Construir el resultado
    result = {
        'id': vino['id'],
        'nombre': vino['nombre'],
        'bodega': bodega,
        'cepas': cepasNombre,
        'partidas': vino['partidas']
    }

    jsonResult = json.dumps(result, ensure_ascii=False)
    return Response(jsonResult, mimetype='application/json')

#EJERCICIO 4
@app.route('/api/vinos', methods=['GET'])
def getVinosPorAnio():
    anio = request.args.get('anio', type=int)
    orden = request.args.get('orden', default='nombre')
    reverso = request.args.get('reverso', default='no') == 'si'

    #Filtramos los vinos que tegan el año especificado en partidas
    vinosFiltrados = [v for v in data['vinos'] if anio in v['partidas']]

    #Ordenamos los vinos
    vinosFiltrados.sort(key=lambda v: v[orden], reverse=reverso)

    #Construimos la lista
    result = []
    for vino in vinosFiltrados:
        bodega = next((b['nombre'] for b in data['bodegas'] if b['id'] == vino['bodega']), 'bodega desconocida')
        cepasNombres = [c['nombre'] for c in data['cepas'] if c['id'] in vino['cepas']]


        result.append({
            'id': vino['id'],
            'nombre': vino['nombre'],
            'bodega': bodega,
            'cepas': cepasNombres,
            'partidas': vino['partidas']

        })

    jsonResult = json.dumps(result, ensure_ascii=False)
    return Response(jsonResult, mimetype='application/json')

#EJERCICIO 5
@app.route('/api/vinos', methods=['GET'])
def getVinosPorAnioFiltrados():
    anio = request.args.get('anio', type=int)
    orden = request.args.get('orden', default='nombre')
    reverso = request.args.get('reverso', default='no') == 'si'

    #Filtramos los vinos que tegan el año especificado en partidas
    vinosFiltrados = [v for v in data['vinos'] if anio in v['partidas']]

    #Ordenamos los vinos
    vinosFiltrados.sort(key=lambda v: v[orden], reverse=reverso)

    #Construimos la lista
    result = []
    for vino in vinosFiltrados:
        bodega = next((b['nombre'] for b in data['bodegas'] if b['id'] == vino['bodega']), 'bodega desconocida')
        cepasNombres = [c['nombre'] for c in data['cepas'] if c['id'] in vino['cepas']]


        result.append({
            'id': vino['id'],
            'nombre': vino['nombre'],
            'bodega': bodega,
            'cepas': cepasNombres,
            'partidas': vino['partidas']

        })

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)