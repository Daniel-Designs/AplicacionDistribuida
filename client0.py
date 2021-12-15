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

headers = {
    'Content-Type': 'application/json',
}

#data = '{"num1" : [1, 2, 3], "num2":[4, 5, 6]}'


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\t\tHola Bienvenido a esta TIENDA VIRTUAL DISTRIBUIDA \n\n")
usuario = input("Por favor Digita tu nombre: ")
print("\n\n")
print("Hola "+ usuario + " este es nuestro Menu de operaciones.\n\n")
repetir = 'si'

while repetir == 'si':
    print("\t 1.Listar Productos\t 2.Comprar Productos\tPagar 3.productos\n\n")
    print("\t\t\t\t Por favor seleccione una opcion\n\n")
    
    try:
        menu = int(input("Numero del Menu: "))
    except:
        print("\n 2---------Recuerda que solo se permiten numeros enteros----------")
        menu = 0
        
    print("\n\n")

    if menu == 1:
        print('\t\t\t<Listar Productos:>  \n\n')
        try:
            response = requests.get('http://10.95.1.4:8080/listarProductos', headers=headers)
            #response = requests.get("http://localhost:8080/listarProductos", headers=headers)
            djson = response.json()
            print(djson)
            see(djson)
            print()
        except:
            print("3 El error fue: ",sys.exc_info()[0])

    elif menu == 2:
        print('\t\t\t\tSeccion <Comprar Productos>: \n\n')
        print('Por favor ingreda el numero de producto que deseas comprar: \n\n')
        ID= input('Numero de ID del producto:   ')
        print("\n\n")
        try:
            numeroArticulos = int(input("Ingresa la cantidad de articulos que deseas adquirir:  "))
            confirmacion = input("\n\nConfirma tu compra escribiendo <si>")
        except:
            print(" 4Recuerda que deben ser numeros positivos enteros")
            confirmacion = "no"
        
        
        if confirmacion == 'si':
            producto = {'ID': ID,'NAME':'Producto'+ID, 'CANTIDAD': numeroArticulos, 'USUARIO':usuario}
            #print(producto+"\n\n") 
            #seeList(ticketsCompra)
            try:
                #response = requests.post('http://10.95.1.4:8080/comprarProductoByID', json = producto)
                response = requests.post('http://localhost:8080/comprarProductoByID', json = producto)
                djson = response.json()
                
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
            
            
    elif menu == 3:
        print('\t\t\t\tSeccion <Pagar Productos>: \n\n')
        if len(ticketsCompra)>0:
            print('Tienes registradas las siguientes compras: \n\n')
            seeList(ticketsCompra)
            pagar = input('Deseas pagar tus compras si/no \n\n')
            if pagar == 'si':
                tarjeta = input("Ingresa los 16 numero de tu tarjeta de credito:  ")
                datos = {'TARJETA':tarjeta,'TICKETSCOMPRA':ticketsCompra}
                print(datos)
                try:    
                    response = requests.post('http://10.95.1.4:8080/pagarProductoByID', json = datos)
                    #response = requests.post('http://localhost:8080/pagarProductoByID', json = datos)
                    djson = response.json()
                    print(djson)    
                    ticketsCompra = []
                except:
                    print("El error fue: ",sys.exc_info()[0])   
        else: 
            print("Por el momento no tienes ninguna compra asociada\n\n"); 
            
            
    else :
        print('Menu no valido por favor selecciona otra opcion\n\n')
        
    print("\n\n Deseas Repetir el menu pricipal\n\n")
    repetir =input("si/No: ")
    print("\n\n")
    
    