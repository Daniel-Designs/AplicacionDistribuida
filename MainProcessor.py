import requests
import json

class ServerFunctions:    

    def listarProductos(self):
        headers = {
            'Content-Type': 'application/json',
        }
        
        #data = '{"num1" : [1, 2, 3], "num2":[4, 5, 6]}'
        #response = requests.post('http://10.95.1.79:8080/suma', headers=headers, data=data)
        #djson = response.json()
        #djson = json.loads(djson)
        #print(djson)

        response = requests.get('http://10.95.1.79:8080/listarProductos', headers=headers)
        djson = response.json()
        print(djson)

        return djson

    def comprarProductoByID(self, producto):
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get('http://10.95.1.79:8080/listarProductos', headers=headers)
        productos = response.json()
        print(productos)
        for producto in productos:
            print(producto)
            print("yes")
            if(producto['ID'] == producto['ID']):
                return producto
                
            
        