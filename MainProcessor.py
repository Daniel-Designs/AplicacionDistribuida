import requests
import json

class ServerFunctions:    

    def listarProductos(self):
        headers = {
            'Content-Type': 'application/json',
        }

        data = '{"num1" : [1, 2, 3], "num2":[4, 5, 6]}'
        response = requests.post('http://10.95.1.4:8080/suma', headers=headers, data=data)
        djson = response.json()
        djson = json.loads(djson)
        print(djson)

        response = requests.get('http://10.95.1.4:8080/listarProductos', headers=headers)
        djson = response.json()
        print(djson)

        return djson


    def suma(self, df): 
        df['sum'] = df.sum(axis=1)
        return  df
        