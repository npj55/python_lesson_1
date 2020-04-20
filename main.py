import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
responce = requests.get(url)
data = json.loads(responce.text)
print (data)