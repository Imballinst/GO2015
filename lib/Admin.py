# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb
from webob import *

import Post
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

# Class Admin    

class Admin(webapp2.RequestHandler):
    def get(self):
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
        
        template = JINJA_ENVIRONMENT.get_template('/admin/dashboard.html')
        self.response.write(template.render(template_values))

    def post(self):
        form = self.request.get('submitType')
        title = None
        content = None
        exp = self.request.cookies.get('expire')
        logging.info(exp)

        if (exp != None):
            valid = CookieManager.checkCookie(exp)
        else:
            valid = 0

        if form == 'submitPost':
            title = self.request.get('title')
            content = self.request.get('content')
            
            # Instantiate Blog class
            postObject = Post.Post()
            
            # Insert the attributes to data store
            postObject.insertToDatastore(title, content)

        # Loads the page
        template_values = {
            'valid': valid,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/dashboard.html')
        self.response.write(template.render(template_values))