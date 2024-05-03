#FastAPI 


- FastAPI é o framework que iremos usar para criar nosso back-end
- Precisamos importar o pacote para dentro do nosso arquivo

```python

from fastapi import FastAPI

```

- Precisamos criar uma aplicação

```python

from fastapi import FastAPI

app = FastAPI()

```

- Criamos uma rota "padrão", que será a nossa rota para a nossa "home" quando digitamos por exemplo "www.site.com" que nos levará direto para o início da página, e não para um subdiretório

```python

from fastapi import FastAPI

app = FastAPI()

@app.get('/') #Esse é um decorator

async def root(): #Esse nosso programa rodará de forma assíncrona.
	return{"message": "Hello World"}
```

- Para rodar nosso servidor no terminal, nós iremos usar o comando: $uvicorn server(nome do nosso arquivo):app(nome da nossa aplicação) --reload(para garantir que todas as mudanças sejam feitas)
