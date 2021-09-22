from flask import Flask, request
import ModelVacinacao

app = Flask("Vacinação")

@app.route("/",methods=['GET'])
def index():
    document = ModelVacinacao
    #resposta = document.selecionarTotalCadastrado()
    totalM = document.selecionarPorSexoMasculino()
    totalF = document.selecionarPorSexoFeminino()
    totalIdade18a24 = document.selecionarPorIdade18a24()
    totalIdade25a60 = document.selecionarPorIdade25a60()
    totalIdadeMaiorque61 = document.selecionarPorIdadeMaiorQue61()
    totalPrimeiradose = document.selecionarPrimeiraDose()
    totalSegundadose = document.selecionarSegundaDose()
    ultimo_dado = document.pega_ultimo_dado()
    cidades = document.pega_as_cidade()
    idade = document.pega_idade()

    return {#"total":resposta,
                "total_masculino":totalM,
                "total_feminino":totalF,
                "total_idade_18a24":totalIdade18a24,
                "total_idade_25a60":totalIdade25a60,
                "total_idade_Maiorque61":totalIdadeMaiorque61,
                "cidades":cidades,
                "idade":idade,
                "total_primeira_dose":totalPrimeiradose,
                "total_segunda_dose":totalSegundadose,
                "ultimo_dado":ultimo_dado
            }

@app.route('/busca',methods=['POST'])
def buscaCidade():
    body = request.get_json()
    document = ModelVacinacao
    totalCidade = document.selecionarPorCidade(body['resposta'])
    print(body)

    return {'total_cidade':totalCidade}

@app.route('/cidade',methods=['GET'])
def cidade():
    body = request.get_json()
    print(body['city'])
    document = ModelVacinacao
    resposta = document.buscar_por_cidade(body['city'])
    cidades = document.pega_as_cidade()
    print(resposta)
    return{'resposta':resposta,'cidades':cidades,'pesquisado':body['city']}

@app.route('/idade',methods=['GET'])
def idade():
    document = ModelVacinacao
    resposta = document.pega_idade()
    cidades = document.pega_as_cidade()


    return {'resposta':resposta,'cidades':cidades}




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)