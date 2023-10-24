import requests
import json
response=requests.put('http://httpbin.org/put', data={'key':'value'})
rtastr=response.content.decode()
print(type(rtastr)) 
rta=json.loads(rtastr)
rta=response.json() 
print(type(rtastr)) 
print(rtastr)
