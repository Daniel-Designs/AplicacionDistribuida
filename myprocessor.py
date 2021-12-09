class sumaMulti:    

productos = [{'ID': '1','NAME':'Producto1'},
                {'ID': '1','NAME':'Producto1'},
                {'ID': '1','NAME':'Producto1'},
                {'ID': '1','NAME':'Producto1'},
                {'ID': '1','NAME':'Producto1'}]
                
    def listarProductos(self):
        return productos

    def suma(self, df): 
        df['sum'] = df.sum(axis=1)
        return  df
        