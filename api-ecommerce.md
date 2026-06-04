# Design da API RESTful: E-commerce Simples

## 1. Design dos Endpoints REST

### Entidade: Produtos
* `GET /api/v1/produtos`: Retorna a lista de produtos.
* `GET /api/v1/produtos/{id}`: Retorna os detalhes de um produto específico.
* `POST /api/v1/produtos`: Cria um novo produto.
* `PUT /api/v1/produtos/{id}`: Atualiza um produto existente.
* `DELETE /api/v1/produtos/{id}`: Remove um produto.

### Entidade: Pedidos
* `GET /api/v1/pedidos`: Retorna a lista de pedidos.
* `GET /api/v1/pedidos/{id}`: Retorna os detalhes de um pedido.
* `POST /api/v1/pedidos`: Cria um novo pedido.
* `PATCH /api/v1/pedidos/{id}/status`: Atualiza apenas o status de um pedido.

---

## 2. Exemplos de Requisição e Resposta completos (com HATEOAS)

### Exemplo 1: Criar um novo Pedido (POST)

**Requisição:**
```http
POST /api/v1/pedidos HTTP/1.1
Host: api.ecommerce.com
Content-Type: application/json

{
  "produto_id": 105,
  "quantidade": 2
}

HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 992,
  "produto_id": 105,
  "quantidade": 2,
  "total": 150.00,
  "status": "pendente",
  "_links": {
    "self": { "href": "/api/v1/pedidos/992" },
    "produto": { "href": "/api/v1/produtos/105" },
    "cancelar": { "href": "/api/v1/pedidos/992", "method": "DELETE" }
  }
}

### Exemplo 2: Buscar detalhes de um Produto (GET)

GET /api/v1/produtos/105 HTTP/1.1
Host: api.ecommerce.com
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 105,
  "nome": "Teclado Mecânico",
  "preco": 75.00,
  "categoria": "Periféricos",
  "estoque": 42,
  "_links": {
    "self": { "href": "/api/v1/produtos/105" },
    "comprar": { "href": "/api/v1/pedidos", "method": "POST" }
  }
}

3. Implementação de HATEOAS
Como demonstrado nos exemplos acima, a API implementa HATEOAS (Hypermedia as the Engine of Application State) retornando um objeto _links no final das respostas. Isso permite que o cliente navegue pela API dinamicamente, descobrindo quais ações podem ser tomadas em seguida (como visualizar o produto do pedido ou cancelar o pedido) baseadas no estado atual do recurso.

4. Estrutura de Tratamento de Erros
A API utilizará um formato padronizado de erro para garantir previsibilidade aos clientes.

Exemplo de Resposta de Erro (404 Not Found):

HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "erro": {
    "codigo": 404,
    "mensagem": "Produto com ID 9999 não encontrado.",
    "detalhes": "Verifique se o ID passado na URL está correto."
  },
  "timestamp": "2026-06-04T13:26:50Z"
}

## Exercício 4: Implementação de API REST com FastAPI

No arquivo `main.py`. Pacotes necessários rodando `pip install fastapi uvicorn pydantic` e, para testar a aplicação, rode `uvicorn main:app --reload`.