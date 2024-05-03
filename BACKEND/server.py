from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Aqui nos criamos uma operação do tipo GET com o endereço "/" q será associado a função home logo abaixo e retornará oque estiver la dentro
def home():
    return{"message": "Hello World caraio, vambora porra"}

@app.get("/Profile")#Aqui nós criamos OUTRA operação do tipo GET só que com o endereço de "/Profile" que irá nos retornar um dicionário com uma chave nome
def profile():
    return{"nome": "Daniel Zanotelli"}

@app.get('/saudacao/{nome}') #Criamos uma outra operação com um parâmetro de rota, que nos retornará o valor especificado
def saudacao(nome: str): #Podemos especificar o tipo de dado com que estamos trabalhando
    texto = f'Olá {nome}! Seja bem-vindo.'
    return{'mensagem': texto} #Usamos o recurso de f-strings do python para retornar um dicionário um pouco mais elaborado