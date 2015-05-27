# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb
from pytz import timezone

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

# Class PostMenu    

class PostMenu(webapp2.RequestHandler):
    def get(self):
        # Cookie check
        exp = self.request.cookies.get('expire')
        logging.info(exp)

        if (exp != None):
            valid = CookieManager.checkCookie(exp)
        else:
            valid = 0

        # Define variables
        postObject = Post.Post()
        posts = postObject.listPosts()
        count = len(posts)
        
        # List
        postIDList = []
        titleList = []
        contentList = []
        datetimeList = []
        
        # Timezone convertion
        # Set timezone
        jkt = timezone('Asia/Jakarta')
        utc = timezone('UTC')

        # For post in posts ...
        for post in posts:
            # Convert timezone
            utc_dt = utc.localize(post.date)
            jkt_dt = utc_dt.astimezone(jkt)

            content = post.content
            
            if (len(content) > 50):
                content = content[:50] + "..."

            # Insert to list
            titleList.append(post.title)
            contentList.append(content)
            datetimeList.append(jkt_dt.strftime("%d-%m-%Y %H:%M:%S"))
            postIDList.append(post.key.id())

        # Loads the page
        template_values = {
            'valid': valid,
            'count': count,
            'titleList': titleList,
            'contentList': contentList,
            'datetimeList': datetimeList,
            'postIDList': postIDList,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/post-menu.html')
        self.response.write(template.render(template_values))

    def post(self):
        # Check cookie
        exp = self.request.cookies.get('expire')
        logging.info(exp)

        if (exp != None):
            valid = CookieManager.checkCookie(exp)
        else:
            valid = 0

        form = self.request.get('submitType')
        title = None
        content = None

        if form == 'submitPost':
            title = self.request.get('title')
            content = self.request.get('content')
            
            # Instantiate Blog class
            postObject = Post.Post()
            
            # Insert the attributes to data store
            postObject.insertToDatastore(title, content)

        # Define variables
        postObject = Post.Post()
        posts = postObject.listPosts()
        count = len(posts)
        
        # List
        postIDList = []
        titleList = []
        contentList = []
        datetimeList = []
        
        # Timezone convertion
        # Set timezone
        jkt = timezone('Asia/Jakarta')
        utc = timezone('UTC')

        # For post in posts ...
        for post in posts:
            # Convert timezone
            utc_dt = utc.localize(post.date)
            jkt_dt = utc_dt.astimezone(jkt)

            content = post.content
            logging.info(len(content))

            if (len(content) > 50):
                content = content[:50] + "..."

            # Insert to list
            titleList.append(post.title)
            contentList.append(content)
            datetimeList.append(jkt_dt.strftime("%d-%m-%Y %H:%M:%S"))
            postIDList.append(post.key.id())

        # Loads the page
        template_values = {
            'valid': valid,
            'count': count,
            'titleList': titleList,
            'contentList': contentList,
            'datetimeList': datetimeList,
            'postIDList': postIDList,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/post-menu.html')
        self.response.write(template.render(template_values))