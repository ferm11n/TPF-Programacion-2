from flask import Flask, Response, jsonify
import json

app = Flask(__name__)

#Cargamos los datos desde el archivo JSON
with open('vinoteca.json') as f:
    data = json.load(f)


#BODEGA
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


#CEPAS
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


#VINOS
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

if __name__ == '__main__':
    app.run(debug=True)