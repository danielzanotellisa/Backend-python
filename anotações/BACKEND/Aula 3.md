#FastAPI 

- O nosso programa é uma instância de um objeto

```python
from fastapi import FastAPI

app = FastAPI()  

@app.get("/")
async def root():  
    return{"message": "Hello World caraio, vambora porra"}
```

- No código acima nos realizamos uma operação do tipo GET
	- E entre os parênteses nós estipulamos o caminho
	- O caminho retorna a função root que nos retorna um dicionário
- Podemos acessar a documentação da nossa API adicionando um "/docs" no endereço
- A função do backend é fornecer uma série de operações que são classificadas entre leitura e escrita
	- Elas são enviadas e recebidas através de um JSON