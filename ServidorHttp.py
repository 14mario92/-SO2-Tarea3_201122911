#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 12345

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write('HOLA MUNDO !!<br><br>')
		self.wfile.write('Mario Alejandro Morales Enriquez<br>');
		self.wfile.write('2011 - 22911<br>');
		self.wfile.write('Tarea #3<br>');
		self.wfile.write('Sistemas Operativos 2 - Junio 2015');
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	#print '\n[SO2]Iniciado Servidor Http en puerto ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	#print '\n[SO2]^C recibido, Servidor Http Detenido'
	server.socket.close()
	
