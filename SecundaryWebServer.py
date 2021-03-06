import cherrypy
import pandas as pd
import SecundaryProcessor
import json
p = SecundaryProcessor.ServerFunctions()

class MyWebService(object):

   @cherrypy.expose
   def listarProductos(self):
      output = p.listarProductos() 
      return json.dumps(output)

   @cherrypy.expose
   @cherrypy.tools.json_in()           #Luego por eso no jala
   def pagarProductoByID(self):
      ID = cherrypy.request.json
      output = p.pagarProductoByID(ID) 
      return json.dumps(output)          

   
   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def suma(self):
      data = cherrypy.request.json
      df = pd.DataFrame(data)
      
      output = p.suma(df)
      return output.to_json()


  

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())