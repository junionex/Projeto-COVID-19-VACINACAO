import requests 
from requests.auth import HTTPBasicAuth
import json


url = "https://imunizacao-es.saude.gov.br/_search"
contador = 0

#retorna 10 linhas
def requisicaoPadrao():
    response = requests.get(url, auth=HTTPBasicAuth('imunizacao_public','qlto5t&7r_@+#Tlstigi'))
    return response

#Retorna 1000 linhas
def requisicaoDe1000Linhas():
    payload = json.dumps({
        "size": 1000
    })
    headers = {
        'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
        'Content-Type': 'application/json',
        'Cookie': 'ELASTIC-PROD=1628023376.7.24157.116093'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

#Returna quantas linhas desejar obs:ate 1m
def requisicaoDeQuantasLinhasQueQuiser(x):
    print("Pegando valores"+ str(x))
    url2 = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"
    payload = json.dumps({
        "size": x
    })
    headers = {
        'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
        'Content-Type': 'application/json',
        'Cookie': 'ELASTIC-PROD=1628023376.7.24157.116093'
    }

    response = requests.request("POST", url2, headers=headers, data=payload)
    return response
#Páginação de 5k
def paginacao(x):
    print("páginação de :"+ str(x))
    
    payload = json.dumps({
        "size": 2,
        "from": x,
        "sort": "@timestamp"
    })
    headers = {
        'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
        'Content-Type': 'application/json',
        'Cookie': 'ELASTIC-PROD=1628023376.7.24157.116093'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def imprimirPorPaginacao(vacina,contador):
    valores = vacina['hits']['hits']
    
    for i in valores:
        print((str(contador)+"-")+i['_source']['paciente_endereco_nmMunicipio'] )
        contador += 1


######################-----CODIGO------##############################
#resposta = requisicaoDeQuantasLinhasQueQuiser(10000)

for count in range(4):
    resposta = paginacao(count*5000)
    vacina = resposta.json()
    imprimirPorPaginacao(vacina,contador)

#print (vacina['hits']['hits'])



#print (valores[0]['_source']['paciente_endereco_nmMunicipio'])


   