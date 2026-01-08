import requests

r = requests.get("https://httpbin.org/get")
headers = r.headers()
print (r)