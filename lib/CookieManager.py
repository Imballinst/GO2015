# Libraries used

import os
import cgi
import urllib
import logging

import Cookie, uuid

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

# Class CookieManager

class CookieManager(object):
    cookie = Cookie.SimpleCookie()
    
    def setCookie():
        # Timezone convertion
        # Set timezone
        jkt = timezone('Asia/Jakarta')
        expires = datetime.datetime.now(jkt) + timedelta(minutes=5)
        
        cookie['session'] = str(uuid.uuid4())
        cookie['session']['domain'] = 'ganeshaopen15.appspot.com'
        cookie['session']['path'] = '/'
        cookie['session']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
        
        logging.info("hehe")
        logging.info(cookie['session'])
        logging.info(cookie['session']['domain'])
        logging.info(cookie['session']['path'])
        logging.info(cookie['session']['expires'])