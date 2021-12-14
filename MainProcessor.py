import requests
import json

class ServerFunctions:    
    def listarProductos(self):
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get('http://10.95.1.79:8080/listarProductos', headers=headers)
        djson = response.json()
        print(djson)
        return djson

    def comprarProductoByID(self, pro):
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get('http://10.95.1.79:8080/listarProductos', headers=headers)
        djson = response.json()
        #print(djson)
        productos = djson
        print(productos)
        for producto in productos:
            print(producto)
            if(producto['ID'] == pro['ID']):
                codigoPago = producto['ID'] + pro['USUARIO'] + producto['NAME'] + str(pro['CANTIDAD']) + 'XDF'
                montoAPagar = producto['COST'] * pro['CANTIDAD']
                retorno = {'codigoPago':codigoPago,'montoAPagar':montoAPagar}
                return retorno
                
    def pagarProductoByID(self, productos):
        print(productos)
        #for producto in productos:  
        #print("\n\nEste producto ha sido pagado usando el siguiente metodo de Pago: " + productos['TARJETA'])
        return "\n\n********************* El pago se ha efectuado CORRECTAMENTE **************\n\n \t\t\tGracias por confiar en Nosotros."
    
    
    