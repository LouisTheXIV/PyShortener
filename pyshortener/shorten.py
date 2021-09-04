"""
URL Shortener Library
~~~~~~~~~~~~~~~~~~~~~

PyShortener is a url shortener package which uses HTTP protocol to send requests to lnk.gdn
which is the website also made by me which shortens the url. 

Documentation is at <https://pyshortener.readthedocs.io/en/latest/>.

:copyright: (c) 2021 by JustAnotherCoder.
"""

from requests import *
import os, sys

## the url which requests are being sent to
req_url = "https://lnk.gdn/add"

class Link():
    def __init__(self, response):
        self.r = response

    def html(self):
        return self.r.text

    def link(self):
        text = self.html()
        text = text[40:]
        link = ""
        
        for x in list(text):
            if x != '"': 
                link += x
            else:
                break
        return link

    def status_code(self):
        return self.r.status_code

    def code(self):
        text = self.html()
        text = text[56:]
        code = ""
        
        for x in list(text):
            if x != '"': 
                code += x
            else:
                break
        return code

"""
Invalid URL Exception. 
If you are getting this error it means the URL either didn't return a 2xx or 1xx, or the scheme is invalid.
Correct scheme is https://example.com.
"""
class InvalidURL(Exception):
    def __init__(self, name, message="URL is invalid, it either doesn't exist or its scheme is invalid."):
        self.name = name
        self.message = message
        super().__init__(self.message)

"""
Sends a post request the https://lnk.gdn/add which the data being the link to shorten.
"""
def shorten(url : str):
    data = {
        "link": url
    }

    res = post(req_url, data=data)
    if "Put in a valid link" in res.text:
        raise InvalidURL(url)
    return Link(res)


