import requests
import json

class ServerFunctions:    
    def listarProductos(self):
        headers = {
            'Content-Type': 'application/json',
        }
        try:
            response = requests.get('http://10.95.1.79:8080/listarProductos', headers=headers)
            djson = response.json()
            print(djson)
            return djson
        except:
            response = requests.get('http://10.95.1.140:8080/listarProductos', headers=headers)
            djson = response.json()
            print(djson)
            return djson
            

    def comprarProductoByID(self, pro):
        headers = {
            'Content-Type': 'application/json',
        }
        try:
            response = requests.get('http://10.95.1.79:8080/listarProductos', headers=headers)
            djson = response.json()
            #print(djson)
            productos = djson
        except:
            print("El servidor no 10.95.1.79 no sirve por lo que utilizaremos el 10.95.1.140 ")
            response = requests.get('http://10.95.1.140:8080/listarProductos', headers=headers)
            djson = response.json()
            productos = djson
        
        print(productos)
        for producto in productos:
            print(producto)
            try:
                    
                if(producto['ID'] == pro['ID']):
                    codigoPago = producto['ID'] + pro['USUARIO'] + producto['NAME'] + str(pro['CANTIDAD']) + 'XDF'
                    montoAPagar = producto['COST'] * pro['CANTIDAD']
                    retorno = {'codigoPago':codigoPago,'montoAPagar':montoAPagar}
                    return retorno
                else:
                    raise ValueError("No existe ningun item con el ID seleccionado")
                
            except:
                
                return 'No existe un ningun producto con ID' + pro['ID']
    
    def pagarProductoByID(self, productos):
        try:
            response = requests.post('http://10.95.1.79:8080/pagarProductoByID', json = productos)
            djson = response.json()
            print(djson)    
            return djson
        except:
            response = requests.post('http://10.95.1.140:8080/pagarProductoByID', json = productos)
            djson = response.json()
            print(djson)
            return djson
        
    
                
    '''                    
    def pagarProductoByID(self, productos):
        print(productos['TICKETSCOMPRA'])
        for producto in productos['TICKETSCOMPRA']:  
            print("\n\nEste producto ha sido pagado usando el siguiente metodo de Pago: " + productos['TARJETA'])
        return "\n\n********************* El pago se ha efectuado CORRECTAMENTE **************\n\n \t\t\tGracias por confiar en Nosotros."
    
    '''
    