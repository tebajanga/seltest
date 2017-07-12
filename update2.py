from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://192.168.0.52:8000/outbox/' + str(10)
data = {'chat_found' : '50', 'processed' : '50'}

request = Request(url, urlencode(data).encode(),method='PUT')
#urlopen(request)
json = urlopen(request).read().decode()
print(json)