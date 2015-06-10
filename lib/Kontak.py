# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb

import Saran

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

# Class Kontak

class Kontak(webapp2.RequestHandler):
    def get(self):
        valid = 1

        # When the page first loads, null template
        template_values = {
            'valid': valid,
        }

        template = JINJA_ENVIRONMENT.get_template('/kontak.html')
        self.response.write(template.render(template_values))

    def post(self):
        form = self.request.get('submitType')
        nama = None
        email = None
        saran = None
        valid = 1

        if form == 'submitSaran':
            nama = self.request.get('name')
            email = self.request.get('email')
            saran = self.request.get('saran')
            
            if (nama != '' and email != ''):
                # Instantiate Blog class
                saranObject = Saran.Saran()
                
                # Insert the attributes to data store
                saranObject.insertToDatastore(nama, email, saran)
            else:
                valid = 0

        # When the page first loads, null template
        template_values = {
            'valid': valid,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/kontak.html')
        self.response.write(template.render(template_values))