import requests
r = requests.post('https://api.github.com/user',data={'key':'value'})
r.status_code
200
print(r.url)
print(r.status_code)
print(r.text)