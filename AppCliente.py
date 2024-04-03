from flask import Flask, make_response, jsonify, request
import psycopg2

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

conn = psycopg2.connect(
    dbname="BancoClientes",
    user="postgres",
    password="3112",
    host="localhost"
)

cursor = conn.cursor()

query_create_table = """
    CREATE TABLE IF NOT EXISTS pessoas(
      id SERIAL PRIMARY KEY,
      nome VARCHAR(100),
      rg varchar(20),
      cpf varchar(20)  
    );
"""

cursor.execute(query_create_table)
conn.commit()


def getClientesById(id):
    query = "select * from pessoas where id = %s"
    cursor.execute(query,(id,))
    return cursor.fetchone()

@app.route('/clientes', methods=['GET'])
def getClientes():
    query = "select * from pessoas"
    cursor.execute(query)
    clientes = cursor.fetchall()
    return make_response(jsonify(clientes),200)

@app.route('/clientes/<int:id>', methods=['GET'])
def getCliente(id):
    cliente = getClientesById(id)
    if not cliente:
        return make_response(jsonify({"Erro":"Cliente não encontrado"}),404)
    return make_response(jsonify(cliente),200)

@app.route('/clientes',methods=['POST'])
def addCliente():
    data = request.json
    nome = data.get('nome')
    rg = data.get('RG')
    cpf = data.get('CPF')
    query = "insert into pessoas(nome, rg, cpf) values (%s,%s,%s) returning id"
    cursor.execute(query, (nome, rg, cpf))
    new_id = cursor.fetchone()[0]
    conn.commit()
    return make_response(jsonify({'id': new_id, 'nome': nome, 'RG': rg, 'CPF': cpf}), 201)

@app.route('/clientes/<int:id>',methods=['PATCH'])
def updateCliente(id):
    cliente = getClientesById(id)
    if not cliente:
        return make_response(
            jsonify({'Erro': 'Cliente não encontrado'}), 404)
    data = request.json
    nome = data.get('nome', cliente[1])
    rg = data.get('RG', cliente[2])
    cpf = data.get('CPF', cliente[3])
    query = "UPDATE pessoas SET nome = %s, rg = %s, cpf = %s WHERE id = %s"
    cursor.execute(query, (nome, rg, cpf, id))
    conn.commit()
    return make_response(jsonify({'id': id, 'nome': nome, 'RG': rg, 'CPF': cpf}), 200)

@app.route('/clientes/<int:id>',methods=['DELETE'])
def deleteCliente(id):
    cliente = getClientesById(id)
    if not cliente:
        return make_response(
            jsonify({'Erro': 'Cliente não encontrado'}), 404)
    query = "DELETE FROM pessoas WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    return make_response(jsonify({'Mensagem': 'Cliente excluído com sucesso'}), 200)

app.run()