# Libraries used

import os
import cgi
import urllib
import logging

from datetime import datetime, timedelta

from lib import TentangKami
from lib import JadwalNasional
from lib import JadwalRecurve
from lib import JadwalCompound
from lib import HasilNasional
from lib import HasilRecurve
from lib import HasilCompound
from lib import Kontak
from lib import Post
from lib import Admin

from pytz import timezone

import pytz
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
        # Define variables
        postObject = Post.Post()
        posts = postObject.listPosts()
        count = len(posts)
        
        # Get Delete ID
        deleteID = self.request.get('deleteid')
        
        # Delete Post with Proper ID
        if (deleteID != ''):
            postObject.deletePost(deleteID)
        
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
            
            # Insert to list
            titleList.append(post.title)
            contentList.append(post.content)
            datetimeList.append(jkt_dt)
            postIDList.append(post.key.id())
            
		# Loads the page
        template_values = {
            'count': count,
            'titleList': titleList,
            'contentList': contentList,
            'datetimeList': datetimeList,
            'postIDList': postIDList,
        }
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

# List of HTML files and classes implemented into them
	
application = webapp2.WSGIApplication([
	('/', MainPage, Post),
	('/tentang-kami', TentangKami.TentangKami),
	('/jadwal/nasional', JadwalNasional.JadwalNasional),
	('/jadwal/recurve', JadwalRecurve.JadwalRecurve),
	('/jadwal/compound', JadwalCompound.JadwalCompound),
	('/hasil/nasional', HasilNasional.HasilNasional),
	('/hasil/recurve', HasilRecurve.HasilRecurve),
	('/hasil/compound', HasilCompound.HasilCompound),
	('/kontak', Kontak.Kontak),
    ('/admin/dashboard', Admin.Admin),
], debug=True)