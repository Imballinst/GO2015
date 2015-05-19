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
    
def checkCookie(expire):
    jkt = timezone('Asia/Jakarta')
    # Check Null
    try:
        cookieDate = datetime.strptime(expire, ('%Y-%m-%d %H:%M:%S'))
        dateNow = datetime.now(jkt)
        
        cookieDate = cookieDate.replace(tzinfo=None)
        dateNow = dateNow.replace(tzinfo=None)
        if (cookieDate > dateNow):
            logging.info("Ada cookie")
            return 1
        else:
            logging.info("Udah expire")
            return 0
    except KeyError:
        logging.info("Gak ada cookie")
        return 0