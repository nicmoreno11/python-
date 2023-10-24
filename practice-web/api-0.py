import requests
#cualquier api
lista=[]
url = 'https://api.covidtracking.com/v2/states.json'
response = requests.get(url)
respuesta = response.json()
#print(type(respuesta)) 
for key in lista:
    if key == lista:
        print(key)
        print(lista)

"""for key in respuesta.keys():  
    if key == 'data': 
        for k in respuesta[key]:
            print(type(k))
            for i in k:
                print(k['name'])"""