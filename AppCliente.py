from flask import Flask, make_response, jsonify, request
from ClienteBD import Clientes

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def getClientesById(id):
    for cliente in Clientes:
        if cliente['id'] == id:
            return cliente
    return None

@app.route('/clientes', methods=['GET'])
def getClientes():
    return make_response(
        jsonify(Clientes),200
    )

@app.route('/clientes/<int:id>', methods=['GET'])
def getCliente(id):
    cliente = getClientesById(id)
    if not cliente:
        return make_response(
            jsonify({'Erro':'Cliente não encontrado'}),404
        )
    return make_response(
        jsonify(cliente)
    )

@app.route('/clientes',methods=['POST'])
def addCliente():
    cliente = request.json
    Clientes.append(cliente)
    return make_response(
        jsonify(cliente),201
    )

@app.route('/clientes/<int:id>',methods=['PATCH'])
def updateCliente(id):
    cliente = getClientesById(id)
    if not cliente:
        return make_response(
            jsonify({'Erro':'Cliente não encontrado'}),404
        )
    clienteAtt = request.json
    for item, valor in clienteAtt.items():
        if item != 'id':
            cliente[item] = valor
    return make_response(
        jsonify(cliente),200
    )

@app.route('/clientes/<int:id>',methods=['DELETE'])
def deleteCliente(id):
    cliente = getClientesById(id)
    if not cliente:
        return make_response(
            jsonify({'Erro':'Cliente não encontrado'}), 404
        )
    Clientes.remove(cliente)
    return make_response(
        jsonify({'Mensagem':'Cliente excluído com sucesso'}), 200
    )

app.run()