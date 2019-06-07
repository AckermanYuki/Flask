from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Ola Mundo, bem vindo!!!"

@app.route("/teste/", methods=['GET'])
def teste():
    return "olaaaa"
    
