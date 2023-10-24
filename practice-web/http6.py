import requests 
import json
url = 'https://www.datos.gov.co/resource/fgk8-hnys.json'
argumentos = {'Covid':'2020'}
response=requests.get(url, params=argumentos)
rtastr=response.content.decode()
print(type(rtastr))
rta=json.loads(rtastr)
print(rtastr)