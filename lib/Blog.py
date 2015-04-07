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

# Pre-defined variables

DEFAULT_BLOG_NAME = 'blogGaneshaOpen'

# Blog key

def blog_key(blog_name=DEFAULT_BLOG_NAME):
    return ndb.Key('Blog', blog_name)

# Class Post

class Post(ndb.Model):
    title = ndb.StringProperty(indexed=True)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

# Class Blog

class Blog(webapp2.RequestHandler):    
    def post(self):
        blog_name = DEFAULT_BLOG_NAME
        post = Post(parent=blog_key(blog_name))
        
        post.title = self.request.get('title')
        post.content = self.request.get('content')
        post.put()