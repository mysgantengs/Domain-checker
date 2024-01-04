import socket
import requests
import pprint
import json

Domains = input('masukkan domainnya : ')
IP_results = socket.gethostbyname(Domains)

url = 'https://geolocation-db.com/jsonp/'+IP_results

response = requests.get(url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for k,v in geolocation.items():
    pprint.pprint(str(k)+ ' : ' +str(v))




# print('Domain : '+Domains)
# print('IP Address : '+IP_results)