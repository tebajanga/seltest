from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://192.168.0.53/ww-api/UpdateMessage.php' # Set destination URL here
data = {'id': '1','chat_found' : '50', 'processed' : '50'}     # Set POST fields here

request = Request(url, urlencode(data).encode())
urlopen(request)
#json = urlopen(request).read().decode()
#print(json)