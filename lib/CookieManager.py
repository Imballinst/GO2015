# Libraries used

import os
import cgi
import urllib
import logging

import Cookie, uuid
from datetime import datetime, timedelta

import jinja2
import webapp2

from pytz import timezone

# Path settings

path = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(path, os.pardir))

# Jinja template

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(path),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

c = Cookie.SimpleCookie()

def setCookieValue():
    jkt = timezone('Asia/Jakarta')
    dt = datetime.now(jkt) + timedelta(minutes=5) # Expires in 5 minutes
    c["expire"] = dt.strftime('%Y-%m-%d %H:%M:%S')
    return c["expire"].value
    
def checkCookie():
    jkt = timezone('Asia/Jakarta')
    # Check Null
    try:
        cookieDate = datetime.strptime('%Y-%m-%d %H:%M:%S', c["expire"].value)
        dateNow = datetime.now(jkt)
        dateNow = dateNow.strftime('%Y-%m-%d %H:%M:%S')
        if (cookieDate < dateNow):
            logging.info("Ada cookie")
            return 1
        else:
            logging.info("Udah expire")
            return 0
    except KeyError:
        logging.info("Gak ada cookie")
        return 0
        
# Class CookieManager

class CookieManager:
    def __init__(self, request):
        self.username = request['username']
        self.password = request['password']
    
    def printCookie(self):
        logging.info(self.username)
        logging.info(self.password)