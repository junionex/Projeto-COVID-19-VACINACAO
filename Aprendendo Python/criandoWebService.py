from flask import Flask, request

app = Flask("Youtube")

@app.route("/",methods=['GET'])
def index():
    return {"total": 200}

@app.route("/olamundo",methods=['GET'])
def olaMundo():
    return {"ola":"mundo"}

@app.route("/cadastra/usuario",methods=['POST'])
def cadastraUsuario():
    body = request.get_json()
    print(body)
    return body


app.run()