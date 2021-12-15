import cherrypy
import pandas as pd
import MainProcessor
import json
p = MainProcessor.ServerFunctions()

class MyWebService(object):

   @cherrypy.expose
   def listarProductos(self):
      output = p.listarProductos() 
      return json.dumps(output)           #Chance ya no necesito enviar nada.

   @cherrypy.expose
   @cherrypy.tools.json_in()           #Luego por eso no jala
   def comprarProductoByID(self):
      producto = cherrypy.request.json
      output = p.comprarProductoByID(producto) 
      return json.dumps(output)          
 
   @cherrypy.expose
   @cherrypy.tools.json_in()           #Luego por eso no jala
   def pagarProductoByID(self):
      ID = cherrypy.request.json
      output = p.pagarProductoByID(ID) 
      return json.dumps(output)          

   @cherrypy.expose
   def listar(self):
      output = p.listar() 
      return json.dumps(output)           #Chance ya no necesito enviar nada.


  

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())