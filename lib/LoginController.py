# Libraries used

import os
import cgi
import urllib
import logging

import jinja2
import webapp2

import CookieManager

# Path settings

path = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(path, os.pardir))

# Jinja template

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Class LoginController

class LoginController(webapp2.RequestHandler):
    # Action to GET request -- Logout
    def get(self):
        exp = self.request.cookies.get('expire')
        logging.info(exp)

        if (exp != None):
            valid = CookieManager.checkCookie(exp)
        else:
            valid = 0

        template_values = {
            'valid': valid,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/login.html')
        self.response.write(template.render(template_values))