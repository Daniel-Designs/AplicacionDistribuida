class sumaMulti:    
    def listarProductos(self):
        productos = [{'ID': '1','NAME':'Producto1'},
        {'ID': '2','NAME':'Producto2'},
        {'ID': '3','NAME':'Producto3'},
        {'ID': '4','NAME':'Producto4'},
        {'ID': '5','NAME':'Producto5'},
        {'ID': '6','NAME':'Producto6'}]
        return productos

    def suma(self, df): 
        df['sum'] = df.sum(axis=1)
        return  df
        