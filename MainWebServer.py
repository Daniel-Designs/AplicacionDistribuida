import cherrypy
import pandas as pd
import myprocessor
p = myprocessor.sumaMulti()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def listarProductos(self):
      output = p.listarProductos
      return output.to_json

 '''  @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def compraArticulo(self):
   
   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def pagaProducto(self):'''
   
   
   
   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def suma(self):
      data = cherrypy.request.json
      df = pd.DataFrame(data)
      
      output = p.suma(df)
      return output.to_json()

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def resta(self):
      data = cherrypy.request.json
      df = pd.DataFrame(data)
      output = p.resta(df)
      return output.to_json()
   

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def multiplicacion(self):
      data = cherrypy.request.json
      df = pd.DataFrame(data)
      output = p.multiplicacion(df)
      return output.to_json() 

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def div(self):
      data = cherrypy.request.json
      df = pd.DataFrame(data)
      output = p.div(df)
      return output.to_json() 

  

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())