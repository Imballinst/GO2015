# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb

import Post

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

# Pre-defined variables

DEFAULT_BLOG_NAME = "blogGaneshaOpen"

# Class Admin    

class Admin(webapp2.RequestHandler):
    def get(self):
        valid = 0
        
		# Loads the page
        template_values = {
            'valid': valid,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/dashboard.html')
        self.response.write(template.render(template_values))

    # Action to POST request
    def post(self):
        # Variables
        form = self.request.get('submitType')
        valid = 0
        user = None
        passw = None
        title = None
        content = None
        
        if form == 'validasi':
            user = self.request.get('user')
            passw = self.request.get('pass')
            logging.info(user)
            logging.info(passw)
            if ((user == 'panitiago2015') and (passw == 'semangka')):
                valid = 1
            else:
                valid = 2
        else:
            title = self.request.get('title')
            content = self.request.get('content')
            
            # Instantiate Blog class
            postObject = Post.Post()
            
            # Insert the attributes to data store
            postObject.insertToDatastore(title, content)
        
        # Reload the page with null template
        template_values = {
            'valid': valid,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/dashboard.html')
        self.response.write(template.render(template_values))