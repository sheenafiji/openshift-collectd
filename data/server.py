#!/usr/bin/env python
 
import BaseHTTPServer
import SimpleHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("127.11.47.5", 7873)
handler.cgi_directories = ["","/cgi"]


 
httpd = server(server_address, handler)
httpd.serve_forever()
