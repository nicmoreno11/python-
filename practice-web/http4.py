#Crecion de API con una imagen cualquiera. 
import requests
url = 'https://cdn-images-1.medium.com/v2/resize:fit:480/1*jA64NTovT-efZ96tcq-X5g.png'
response =requests.get(url,stream=True)

#abre un archivo nuevo, ese archivo es una imagen llamada 'kotlinpng'.
with open('practice-web/imgkotlin.png','wb') as kotlinpng:
    for i in response.iter_content():
        kotlinpng.write(i)
        