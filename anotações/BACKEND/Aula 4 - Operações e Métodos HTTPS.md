#FastAPI 

- a Web moderna é baseada em API REST
- Podemos fazer 4 operações principais
	- GET: Solicitamos algo, pegamos informação de algo
	- POST: Usado para ENVIAR informações para o servidor
	- PUT:  Quando queremos atualizar uma informação já existente em um servidor
	- DELETE: Quando queremos remover um item do servidor
- Essas são apenas recomendações, podemos fazer uma aplicação inteira somente com uma operação
- Temos o conceito de ROTA nas aplicações BackEnd
	- Basicamente, junto dos métodos, representam uma funcionalidade do nosso aplicativo
	- Em FastAPI, nós definimos o nosso PATH (rota) quando criamos a nossa requisição
	```python
	app.get("nome da rota")
```
	- Conhecido também como ENDPOINT
- Podemos criar operações diferentes com métodos diferentes para a mesma rota, desde que elas tenha um método diferente.
- Podemos configurar as nossas rotas e dar mais poder para elas
	```python
	app.get('/saudacao/{nome}')
	def saudacao(nome: str):
		return nome
```
	- Podemos usar um parâmetro para tornar a nossa rota possa ser configurável
	- Podemos também indicar o tipo do parâmetro
	- A partir disso,  nós podemos usar recursos  do python para construir melhor a nossa resposta.
	- Devemos tomar cuidado utilizando isso porque caso o tipo errado de dado seja passado, receberemos um erro.