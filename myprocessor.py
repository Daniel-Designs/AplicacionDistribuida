class sumaMulti:    

    def suma(self, df): 
        df['sum'] = df.sum(axis=1)
        return  df
        
    def multiplicacion(self, df):        
        df['mul']=df['num1']*df['num2']
        return df
    def resta(self, df): 
        df['rest'] = df['num1']-df['num2']
        return  df
        
    def div(self, df):        
        df['div']=df['num1']/df['num2']
        df.head()
        return df
    