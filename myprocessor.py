class sumaMulti:    



    def listarProductos(self):
        productos = {'ID': '1','NAME':'Producto1'}
        return productos

    def suma(self, df): 
        df['sum'] = df.sum(axis=1)
        return  df
        