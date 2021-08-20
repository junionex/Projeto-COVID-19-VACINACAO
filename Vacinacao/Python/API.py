from flask import Flask, request
import ModelVacinacao

app = Flask("Vacinação")

@app.route("/",methods=['GET'])
def index():
    document = ModelVacinacao
    resposta = document.selecionarTotalCadastrado()
    totalM = document.selecionarPorSexoMasculino()
    totalF = document.selecionarPorSexoFeminino()
    totalIdade18a24 = document.selecionarPorIdade18a24()
    totalIdade25a60 = document.selecionarPorIdade25a60()
    totalIdadeMaiorque61 = document.selecionarPorIdadeMaiorQue61()
    totalPrimeiradose = document.selecionarPrimeiraDose()
    totalSegundadose = document.selecionarSegundaDose()
    return {"total":resposta,
            "total_masculino":totalM,
            "total_feminino":totalF,
            "total_idade_18a24":totalIdade18a24,
            "total_idade_25a60":totalIdade25a60,
            "total_idade_Maiorque61":totalIdadeMaiorque61,
            "total_primeira_dose":totalPrimeiradose,
            "total_segunda_dose":totalSegundadose
            }

@app.route('/',methods=['POST'])
def buscaCidade():
    body = request.get_json()
    document = ModelVacinacao
    totalCidade = document.selecionarPorCidade(body['resposta'])
    print(body)

    return {'total_cidade':totalCidade}


app.run()