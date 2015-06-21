#!/usr/bin/env python
__author__ = 'bing'


class HttpResponse:
    """HttpResponse contains http response headers and body content."""
    header_end = "\n"

    def __init__(self):
        self.headers = []
        self.content = ""
        self.response = ""
        self.status_code = ""

    def add_status_code(self, status_code=""):
        self.status_code = status_code

    def add_header(self, header):
        self.headers.append(header)

    def add_content(self, content):
        self.content = content

    def __str__(self):
        self.response = self.status_code
        for header in self.headers:
            self.response += header

        self.response += self.header_end
        self.response += self.content
        return self.response