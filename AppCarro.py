#Importação de itens e bibliotecas externas
from flask import Flask, make_response, jsonify, request
from bd import Carros

#Criação das variáveis e configurações
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#Função de apoio
def getCarroById(id):
    for carro in Carros:
        if carro['id'] == id:
            return carro
    return None

#Função para listar todos os carros da lista
@app.route('/carros', methods=['GET'])
def getCarros():
    return make_response(
        jsonify(Carros),200
    )

#Função para buscar por um carro dentro da lista, por ID
@app.route('/carros/<int:id>',methods=['GET'])
def getCarro(id):
    carro = getCarroById(id)
    if not carro:
        return make_response(
            jsonify({'Erro': 'Carro não encontrado'}), 404
        )
    return make_response(
        jsonify(carro)
    )

#Função para adicionar um carro a lista
@app.route('/carros',methods=['POST'])
def createCarro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(carro),201
    )
    

#Função para alterar um carro da lista
@app.route('/carros/<int:id>',methods=['PATCH'])
def updateCarro(id):
    carro = getCarroById(id)
    if not carro:
        return make_response(
            jsonify({'Erro':'Carro não encontrado'}),404
        )
    carroAtt = request.json
    for iten, valor in carroAtt.items():
        if iten != 'id':
            carro[iten] = valor
    return make_response(
        jsonify(carro),200
    )   
    
#Função para deletar um carro da lista
@app.route('/carros/<int:id>',methods=['DELETE'])
def deleteCarro(id):
    carro = getCarroById(id)
    if not carro:
        return make_response(
            jsonify({'Erro':'Carro não encontrado'}),404
        )
    Carros.remove(carro)
    return make_response(
        jsonify({'Mensagem':'Carro deletardo com sucesso'}),200
    )
    
app.run()