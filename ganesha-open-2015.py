# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb

from lib import About

import jinja2
import webapp2

# Path settings

path = os.path.dirname(__file__)
subpath = path

# Jinja template

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader([path,subpath]),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

# Class MainPage

class MainPage(webapp2.RequestHandler):
	def get(self):
		# When the page first loads, null template
		template_values = {}
		
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))

# List of HTML files and classes implemented into them
	
application = webapp2.WSGIApplication([
	('/', MainPage),
	('/about.html', About.About),
], debug=True)