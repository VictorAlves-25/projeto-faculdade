from flask import Flask

app = Flask(__name__)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def saudacao(nome):
    return f"Olá, {nome}!"

@app.route("/")
def home():
    return "Aplicacao rodando com sucesso"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
