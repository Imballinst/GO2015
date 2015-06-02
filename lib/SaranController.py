# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb
from pytz import timezone

import jinja2
import webapp2

import CookieManager
import Saran

# Path settings

path = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(path, os.pardir))

# Jinja template

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Class SaranController

class SaranController(webapp2.RequestHandler):
    def get(self):
        # Check cookie
        exp = self.request.cookies.get('expire')
        logging.info(exp)

        if (exp != None):
            valid = CookieManager.checkCookie(exp)
        else:
            valid = 0

        saranObject = Saran.Saran()
        
        # Get Delete ID
        deleteID = self.request.get('deleteid')

        # Delete Saran with Proper ID
        if (deleteID != ''):
            saranObject.deleteSaran(deleteID)
            source = 'saran'

            # When the page first loads, null template
            template_values = {
                'valid': valid,
                'source': source,
            }
            
            template = JINJA_ENVIRONMENT.get_template('/redirect.html')
            self.response.write(template.render(template_values))