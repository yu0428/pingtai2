#!/usr/bin/env python
__author__ = 'bing'


class HttpRequest:
    def __init__(self):
        self.method = ""
        self.cookie = ""
        self.query_string = ""
        self.accept = ""
        self.request_uri = ""