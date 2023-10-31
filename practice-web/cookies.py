import requests
url = 'http://httpbin.org/cookies'
mycookies = {
    'cookies':'True'
}
response = requests.get(url, cookies=mycookies)
print(response.content)
print('-'*50)

