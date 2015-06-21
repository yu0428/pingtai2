#!/usr/bin/env python
__author__ = 'bing'

import cgi
import cgitb
import os
from http.httprequest import HttpRequest
from http.httpreponse import HttpResponse
from confparser import ConfParser


cgitb.enable(display=0, logdir=".", format="text")  # for troubleshooting


def load_class(class_name):
    # calss_name must be fully qualified class name.

    last_dot = class_name.rfind(".")
    module_name = class_name[0:last_dot]
    clsname = class_name[last_dot+1:]

    mod = __import__(module_name, fromlist=[clsname])
    cls = getattr(mod, class_name[last_dot+1:])
    return cls


class Portal:
    def __init__(self):
        pass

    def create_http_request(self):
        """Create Http Request from os environment variables."""
        http_request = HttpRequest()
        if "REQUEST_METHOD" in os.environ:
            http_request.method = os.environ["REQUEST_METHOD"].strip().lower()
        if "HTTP_COOKIE" in os.environ:
            http_request.cookie = os.environ["HTTP_COOKIE"].strip()
        if "QUERY_STRING" in os.environ:
            http_request.query_string = os.environ["QUERY_STRING"].strip()
        if "HTTP_ACCEPT" in os.environ:
            http_request.accept = os.environ["HTTP_ACCEPT"].strip()
        if "REQUEST_URI" in os.environ:
            http_request.request_uri = os.environ["REQUEST_URI"].strip()

        return http_request

    def handle_request(self):

        http_request = self.create_http_request()
        http_response = HttpResponse()

        field_storage = cgi.FieldStorage()
        action = field_storage.getfirst("action").strip()

        confparser = ConfParser()
        handler_section = confparser.read_section(section="handler")

        try:
            handler_class_name = handler_section[action]
        except KeyError:
            handler_class_name = "view.handler.ErrorPageHandler"

        handler_class = load_class(handler_class_name)
        handler = handler_class()
        handler.handle(http_request, http_response)
        print(http_response)

#print("Content:text/html\n\n")
#for i in os.environ:
#    print '%s => %s' % (i, os.environ[i])

portal = Portal()
portal.handle_request()
