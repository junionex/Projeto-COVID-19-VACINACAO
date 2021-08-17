import requests 
from requests.auth import HTTPBasicAuth
import json


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
        print((str(contador)+"-")+i['_source']['paciente_endereco_nmMunicipio'] +(str("----")) +i['_source']['@timestamp'] )
        contador += 1
        ultimo = i['_source']['@timestamp']
    print("ultimo = " + ultimo)
    return ultimo

######################-----CODIGO------##############################
#resposta = requisicaoDeQuantasLinhasQueQuiser(10000)


#print(resposta)
resposta = requisicao()
f = 1
while(f == 1):
    vacina = resposta.json()
    ultimo = imprimirPorPaginacao(vacina)
    resposta = paginacao(ultimo)
#print (vacina['hits']['hits'])



#print (valores[0]['_source']['paciente_endereco_nmMunicipio'])


   