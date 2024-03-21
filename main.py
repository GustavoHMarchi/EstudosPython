from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def getCarroById(carro_id):
    for carro in Carros:
        if carro['id'] == carro_id:
            return carro
    return None

@app.route('/carros', methods=['GET'])
def getCarros():
    return make_response(
        jsonify(Carros,200)
        )
    
@app.route('/carros', methods=['POST'])
def createCarro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(carro,200)
    )

@app.route('/carros/<int:carro_id>',methods=['PATCH'])
def updateCarro(carro_id):
    carro = getCarroById(carro_id)
    if not carro:
        return make_response(
            jsonify({'Erro':'Carro não encontrado'},404)
        )
    data = request.json
    for key, value in data.items():
        if key != 'id':
            carro[key] = value
    return make_response(
        jsonify(carro,200)
        )
    
@app.route('/carros/<int:carro_id>',methods=['DELETE'])
def deleteCarro(carro_id):
    carro = getCarroById(carro_id)
    if not carro:
        return make_response(
            jsonify({'Erro':'Carro não encontrado'},404)
        )
    Carros.remove(carro)
    return make_response(
        jsonify({'Mensagem':'Carro deletado'},200)
    )

app.run()