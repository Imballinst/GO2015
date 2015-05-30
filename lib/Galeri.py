# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb

import CookieManager

import jinja2
import webapp2

# Path settings

path = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(path, os.pardir))

# Jinja template

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Class PostMenu    

class Galeri(webapp2.RequestHandler):
    def get(self):
        # Cookie check
        exp = self.request.cookies.get('expire')
        logging.info(exp)

        if (exp != None):
            valid = CookieManager.checkCookie(exp)
        else:
            valid = 0

        # Loads the page
        template_values = {
            'valid': valid,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/galeri.html')
        self.response.write(template.render(template_values))

    def post(self):
        # Check cookie
        exp = self.request.cookies.get('expire')
        logging.info(exp)

        if (exp != None):
            valid = CookieManager.checkCookie(exp)
        else:
            valid = 0

        # Loads the page
        template_values = {
            'valid': valid,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/galeri.html')
        self.response.write(template.render(template_values))