import requests
import json
import pandas as pd
from pandas import json_normalize


def see (data1):
    for key in data1:
        print(key +"\t")
        for num in data1[key]:
            print (data1[key][num])
            
menu = 0

headers = {
    'Content-Type': 'application/json',
}

data = '{"num1" : [1, 2, 3], "num2":[4, 5, 6]}'

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Hola Bienvenido a esta TIENDA VIRTUAL DISTRIBUIDA \n\n")
nombre = input("Por favor Digita tu nombre: ")
print("\n\n")
print("Hola "+nombre+ " este es nuestro Menu de operaciones.\n\n")
repetir = 'si'

while repetir == 'si':
    print("\t 1.Listar Productos\t 2.Comprar Productos\tPagar 3.productos\n\n")
    print("Por favor seleccione una opcion\n\n")
    menu = int(input("Numero del Menu: "))
    print("\n\n")

    if menu == 1:
        print('Listar Productos: \n\n')
        response = requests.get('http://10.95.1.4:8080/listarProductos', headers=headers)
        djson = response.json()
        print(djson)
        #see(djson)
        print()

    elif menu == 2:
        print('Comprar Productos: \n\n')
        producto={'ID':'2'}
        response = requests.post('http://10.95.1.4:8080/comprarProductoByID', json=producto)
        djson = response.json()
        print(djson)
        print()
    elif menu == 3:
        print('Pagar Productos: \n\n')
    else :
        print('Menu no valido por favor selecciona otra opcion\n\n')
        
    print("Deseas Repetir el menu pricipal\n\n")
    repetir =input("si/No:   ")
    print("\n\n")
    
    