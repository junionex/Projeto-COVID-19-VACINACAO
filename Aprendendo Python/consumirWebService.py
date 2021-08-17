import json,urllib.request
cep = input('digite o cep: ')
url = "https://viacep.com.br/ws/"+cep+"/json/"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(data)
print(data['cep'])





