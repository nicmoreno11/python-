import requests 
response = requests.delete('http://httpbin.org/delete', data={'key':'value'})
print("La página proporcionada se eliminó correctamente.",

"El código de éxito de la página eliminada es: ", response)