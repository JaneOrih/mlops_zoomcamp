import requests

ride={
    'PUL':30,
    'DOL':50
}

url='http://localhost:9696/predict'
response=requests.post(url,json=ride)
print(response.json())