#HTTP metodo POST
import requests
import json
#url="http://httpbin.org/get?formacion=adso&ficha=2566404"
url='http://httpbin.org/post'
argumentos={'formacion':'adso','ficha':2566404}
myheader = {
    'content-type':'application/jason',
    'acces-token':b'12345'
}
response=requests.post(url, data=json.dumps(argumentos), headers=myheader)
rtastr=response.content.decode()
print(rtastr)