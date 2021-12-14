class ServerFunctions:    
    def listarProductos(self):
        productos = [{'ID': '1','NAME':'Producto1','COST':2300},
        {'ID': '2','NAME':'Producto2','COST':440},
        {'ID': '3','NAME':'Producto3','COST':250},
        {'ID': '4','NAME':'Producto4','COST':3040},
        {'ID': '5','NAME':'Producto5','COST':20},
        {'ID': '6','NAME':'Producto6','COST':333}]
        return productos

    def suma(self, df): 
        df['sum'] = df.sum(axis=1)
        return  df
        