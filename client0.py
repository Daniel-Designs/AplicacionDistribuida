import requests
import json
import pandas as pd
from pandas import json_normalize

def see (data1):
    for key in data1:
        print(key +"\t")
        for num in data1[key]:
            print (data1[key][num])

headers = {
    'Content-Type': 'application/json',
}

data = '{"num1" : [1, 2, 3], "num2":[4, 5, 6]}'
'''
response = requests.post('http://10.95.1.4:8080/suma', headers=headers, data=data)
djson = response.json()
djson = json.loads(djson)
print(djson)
see(djson)
print()'''

response = requests.get('http://10.95.1.4:8080/listarProductos', headers=headers)
djson = response.json()
print(djson)
#see(djson)
print()

