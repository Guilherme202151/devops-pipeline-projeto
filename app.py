from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)


# Rota principal
@app.route("/")
def home():
    return "Hello, DevOps World!"


# Ponto de entrada para rodar localmente
if __name__ == "__main__":
    # host 0.0.0.0 permite acesso externo (útil no container/VM)
    app.run(host="0.0.0.0", port=5000, debug=True)
