# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb

import jinja2
import webapp2

import Post

# Path settings

path = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(path, os.pardir))

# Jinja template

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(path),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

# Class PostController

class PostController(webapp2.RequestHandler):
    def get(self):
        postObject = Post.Post()
        
        # Get Delete ID
        deleteID = self.request.get('deleteid')
        
        # Delete Post with Proper ID
        if (deleteID != ''):
            postObject.deletePost(deleteID)
        
        # When the page first loads, null template
        template_values = {}
        
        template = JINJA_ENVIRONMENT.get_template('/redirect.html')
        self.response.write(template.render(template_values))