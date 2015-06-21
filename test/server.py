#!/usr/bin/env python
__author__ = 'bing'

""" Web server for testing purpose"""

import BaseHTTPServer
import CGIHTTPServer

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()
