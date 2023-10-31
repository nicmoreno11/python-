import requests
s = request.Session()
s.auth('nicmoreno11@misena.edu.co', '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')
response.get('https://api.github.com/users')
print(response.status_code)
if response.ok: #->status_code==200.
    response1=s.get('https://github.com/nicmoreno11')
    print(response1.cookies)

