import requests
s = request.Session()
response=s.get('https://www.recetasnestle.com.co')
print(response.status_code)
if response.ok:
    print(response.cookies)