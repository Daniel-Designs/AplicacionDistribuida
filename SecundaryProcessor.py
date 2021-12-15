class ServerFunctions:    
    def listarProductos(self):
        productos = [{'ID': '1','NAME':'Producto1','COST':2300},
        {'ID': '2','NAME':'Producto2','COST':440},
        {'ID': '3','NAME':'Producto3','COST':250},
        {'ID': '4','NAME':'Producto4','COST':3040},
        {'ID': '5','NAME':'Producto5','COST':20},
        {'ID': '6','NAME':'Producto6','COST':333}]
        return productos

    def pagarProductoByID(self, productos):
        print(productos['TICKETSCOMPRA'])
        for producto in productos['TICKETSCOMPRA']:  
            print("\n\nEste producto ha sido pagado usando el siguiente metodo de Pago: " + productos['TARJETA'])
        return "\n\n********************* El pago se ha efectuado CORRECTAMENTE **************\n\n \t\t\tGracias por confiar en Nosotros."
    
    
    '''
    def suma(self, df): 
        df['sum'] = df.sum(axis=1)
        return  df'''
        