# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb

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

# Class JadwalRecurve

class JadwalRecurve(webapp2.RequestHandler):
	def get(self):
		# When the page first loads, null template
		template_values = {}
		
		template = JINJA_ENVIRONMENT.get_template('/jadwal-recurve.html')
		self.response.write(template.render(template_values))