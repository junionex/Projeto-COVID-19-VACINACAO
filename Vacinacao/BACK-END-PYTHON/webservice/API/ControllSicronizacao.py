import requests 
from requests.auth import HTTPBasicAuth
import json
import ModelVacinacao


url = "https://imunizacao-es.saude.gov.br/_search"
contador = 0

#Páginação de 5k
def requisicao():
    payload = json.dumps({
 	 	"size": 10000,
  		"sort": "@timestamp",
  		"query": {
    		"match": {
      			"estabelecimento_uf": "RN"
    		}
  		}
	})
    headers = {
        'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
        'Content-Type': 'application/json',
        'Cookie': 'ELASTIC-PROD=1628023376.7.24157.116093'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response
def paginacao(x):
    payload = json.dumps({
		"size": 10000,
		"sort": "@timestamp",
		"search_after": [
		    x
		 ],
		  "query": {
		    "match": {
		      "estabelecimento_uf": "RN"
		    }
		  }
	})
    headers = {
        'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
        'Content-Type': 'application/json',
        'Cookie': 'ELASTIC-PROD=1628023376.7.24157.116093'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def imprimirPorPaginacao(vacina):
    valores = vacina['hits']['hits']
    ultimo = ""
    global contador
    for i in valores:
        if(i['_source']['paciente_endereco_uf'] == 'RN'):
            print((str(contador)+"-")+i['_source']['paciente_endereco_nmMunicipio'] +(str("----")) +i['_source']['@timestamp'] )
            document = ModelVacinacao
            conexao = document.getPegarConexao()
            pahfechar = document.getPegarOConn()
            document.addPaciente(conexao, i['_source']['@timestamp'], i['_source']['paciente_idade'], i['_source']['paciente_endereco_nmMunicipio'],i['_source']['vacina_descricao_dose'], i['_source']['vacina_fabricante_nome'], i['_source']['vacina_categoria_nome'], i['_source']['vacina_nome'], i['_source']['paciente_enumSexoBiologico'],i['_source']['document_id'])
            document.fecharConexao(pahfechar,conexao)
            contador += 1
            ultimo = i['_source']['@timestamp']
            sortUltimo = i['sort']
    print("ultimo = " + ultimo + "---sort: " + str(sortUltimo))

    return ultimo

######################-----CODIGO------##############################
#resposta = requisicaoDeQuantasLinhasQueQuiser(10000)


#print(resposta)
def sicronizacao_do_zero():
    resposta = requisicao()
    f = 1
    while(f == 1):
        if(resposta.status_code == 200):
            print('resultado é 200')
            vacina = resposta.json()
            ultimo = imprimirPorPaginacao(vacina)
            resposta = paginacao(ultimo)
        else:
            print("----------------------")
            print(resposta.status_code)
            f = 2

def sicronizacao_do_ultimo():
    document = ModelVacinacao
    ultimo = document.pega_ultimo_dado()
    global contador
    cont = document.selecionarTotalCadastrado()
    contador = cont[0][0]
    ultimo[0][0]
    resposta = paginacao(ultimo[0][0])
    f = 1
    while(f == 1):
        if(resposta.status_code == 200):
            print('resultado é 200')
            vacina = resposta.json()
            ultimo = imprimirPorPaginacao(vacina)
            resposta = paginacao(ultimo)
        else:
            print("----------------------")
            print(resposta.status_code)
            f = 2


sicronizacao_do_ultimo()



   