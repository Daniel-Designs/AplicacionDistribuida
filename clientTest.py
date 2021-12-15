import requests
import json
import sys
import pandas as pd
from pandas import json_normalize


def see (productos):
    print('\n\n \tID \t\t\tNombreProducto \t\t\tPrecio')
    for producto in productos:
        print('\t'+producto['ID']+'\t\t\t'+producto['NAME']+'\t\t\t'+str(producto['COST']))
        print("\n")
        
    print('\n')

def seeList(lista):
    print('\n\n \tID \t\tNombre del Producto\tMonto a Pagar\t Codigo de Pago')
    for lis in lista:
        print('\n\t' + lis['ID'] + '\t\t' + lis['NAME'] + '\t\t' + str(lis['MONTOAPAGAR']) + '\t\t\t' + lis['CODIGOPAGO'])
    print()
    

menu = 0
ticketsCompra = [] 
ticketsCompraTest = [{'ID': '2', 'NAME': 'Producto2', 'CANTIDAD': 3, 'USUARIO': 'da', 'CODIGOPAGO': '2daProducto23XDF', 'MONTOAPAGAR': 1320}]

headers = {
    'Content-Type': 'application/json',
}



print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\t\tHola Bienvenido ********** PRUEBAS DE APP DISTRIBUIDA ************* \n\n")
usuario = 'USERNAMETEST'
repetir = 'si'

while repetir == 'si':
    print("\t 1.Listar Productos\n\n 2.Comprar Productos\t\n\nPagar 3.productos\n\nPagar 4.Listar Productos con delay\n\n")
    print("\t\t\t\t Por favor seleccione una opcion\n\n")
    
    try:
        menu = int(input("Numero del Menu: "))
    except:
        print("\n 2---------Recuerda que solo se permiten numeros enteros----------")
        menu = 0
        
    print("\n\n")

    if menu == 1:
       
        print('\t\t\t<Listar Productos:>  \n\n\t\t\tSe repetira 15 veces  \n\n')
        x=1
        while x < 50:
            try:
                #response = requests.get('http://10.95.1.4:8080/listarProductos', headers=headers)
                response = requests.get("http://localhost:8080/listarProductos", headers=headers)
                djson = response.json()
                print(djson)
                see(djson)
                print()
            except:
                print("3 El error fue: ",sys.exc_info()[0])
            x+=1

    elif menu == 2:
         
        print('\t\t\t\tSeccion <Comprar Productos>: 50 veces \n\n')
        print('Para efectos practicos se realizaran con los valores estaticos ID=4 Cantidad=5 \n\n')
        ID= '5'
        numeroArticulos = 5
        print("\n\n")
        x=0
        while x < 50:
        
            producto = {'ID': ID,'NAME':'Producto'+ID, 'CANTIDAD': numeroArticulos, 'USUARIO':usuario}
                #print(producto+"\n\n") 
                #seeList(ticketsCompra)
            try:
                #response = requests.post('http://10.95.1.4:8080/comprarProductoByID', json = producto)
                response = requests.post('http://localhost:8080/comprarProductoByID', json = producto)
                djson = response.json()
                #print(djson)
                #print("No se de donde viene esto")
                if isinstance(djson,str):
                    print("ups un error")
                    raise ValueError(djson)
                    
                producto['CODIGOPAGO'] = djson['codigoPago']
                producto['MONTOAPAGAR'] = djson['montoAPagar']
                print('\n\nEl monto a pagar sera de: ' + str(producto['MONTOAPAGAR']) + '\n\n')
                ticketsCompra.append(producto)
                seeList(ticketsCompra)
                print("\n\n\t\t*********************Compra generada********************\n\n")
                
            except ValueError :
                print("5 El error fue: ",sys.exc_info()[0])
            x+=1    
            
    elif menu == 3:
        print('\t\t\t\tSeccion <Pagar Productos>: 50 veces \n\n')
        x = 0
        while x < 50:
            if len(ticketsCompraTest)>0:
                print('Tienes registradas las siguientes compras: \n\n')
                seeList(ticketsCompra)
                pagar = 'si'
                if pagar == 'si':
                    tarjeta = '1234 2312 3213 3122'
                    datos = {'TARJETA':tarjeta,'TICKETSCOMPRA':ticketsCompraTest}
                    #print(datos)
                    try:    
                        #response = requests.post('http://10.95.1.4:8080/pagarProductoByID', json = datos)
                        response = requests.post('http://localhost:8080/pagarProductoByID', json = datos)
                        djson = response.json()
                        print(djson)    
                        ticketsCompra = []
                    except:
                        print("El error fue: ",sys.exc_info()[0])   
            else: 
                print("Por el momento no tienes ninguna compra asociada\n\n"); 
            x+=1    
    
    if menu == 4:
       
        print('\t\t\t<Listar Productos con un Delay de 7s:>  \n\n\t\t\tSe repetira 7 veces  \n\n')
        x=0
        while x < 7:
            try:
                #response = requests.get('http://10.95.1.4:8080/listar', headers=headers)
                response = requests.get("http://localhost:8080/listar", headers=headers)
                djson = response.json()
                print(djson)
                see(djson)
                print()
            except:
                print("3 El error fue: ",sys.exc_info()[0])

            x+=1
    
            
    else :
        print('Menu no valido por favor selecciona otra opcion\n\n')
        
    print("\n\n Deseas Repetir el menu pricipal\n\n")
    repetir =input("si/No: ")
    print("\n\n")
    
    