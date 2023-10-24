import requests
url = 'https://www.datos.gov.co/resource/y9ga-zwzy.json'
response = requests.get(url)
print(type(response))