
# API de clientes

API desenvolvida utilizando python para realização de um CRUD de clientes, tendo como objetivo principal o estudo da linguagem Python + Flask



## Documentação da API

#### Endpoints da API:

```http
  GET /clientes
  [retorna todos os clientes cadastrados]
```
```http
  GET /clientes/{id}
  [retorna o cliente cadastrado que possui este id]
```
```http
  POST /clientes
  [cadastra um novo cliente - requer um corpo JSON]
```
```http
  PATCH /clientes/{id}
  [altera um cliente já cadastrado - requer um corpo JSON]
```
```http
  DELETE /clientes/{id}
  [deleta o cliente cadastrado que possui este id]
```
