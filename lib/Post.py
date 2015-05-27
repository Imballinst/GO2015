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

    def listPosts(self):
        # Set variable name
        blog_name = DEFAULT_BLOG_NAME
        
        # Instantiates a query
        posts_query = Post.query(ancestor=blog_key(blog_name)).order(+Post.date)
        
        # Execute the query
        posts = posts_query.fetch(10)
        
        return posts
    
    def insertToDatastore(self, title, content):
        # Set variable name
        blog_name = DEFAULT_BLOG_NAME
        
        # Set datastore name
        post = Post(parent=blog_key(blog_name))
        
        # Input into model's attribute
        post.title = title
        post.content = content

        # Submit
        post.put()
    
    def deletePost(self, postID):
        # Define variables
        blog_name = DEFAULT_BLOG_NAME
        
        # Get the post
        postID = int(postID)
        key = blog_key(blog_name)
        post = Post.get_by_id(postID, parent=key)
        post.key.delete()

    def getPost(self, postID):
        # Define variables
        blog_name = DEFAULT_BLOG_NAME

        # Get the post
        postID = int(postID)
        key = blog_key(blog_name)
        post = Post.get_by_id(postID, parent=key)
        return post

    def updatePost(self, title, content, postID):
        # Set variable name
        blog_name = DEFAULT_BLOG_NAME
        
        # Get the post
        postID = int(postID)
        key = blog_key(blog_name)
        post = Post.get_by_id(postID, parent=key)

        # Edit entity
        post.title = title
        post.content = content

        # Submit
        post.put()