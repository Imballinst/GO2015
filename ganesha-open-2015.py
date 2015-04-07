# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb
from datetime import datetime, timedelta

from lib import TentangKami
from lib import JadwalNasional
from lib import JadwalRecurve
from lib import JadwalCompound
from lib import HasilNasional
from lib import HasilRecurve
from lib import HasilCompound
from lib import Kontak
from lib import Blog
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
        Post = Blog.Blog()
        posts = Post.listPosts()
        count = len(posts)
        
        # List
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
            
		# Loads the page
        template_values = {
            'count': count,
            'titleList': titleList,
            'contentList': contentList,
            'datetimeList': datetimeList,
        }
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

# List of HTML files and classes implemented into them
	
application = webapp2.WSGIApplication([
	('/', MainPage, Blog),
	('/tentang-kami.html', TentangKami.TentangKami),
	('/jadwal-nasional.html', JadwalNasional.JadwalNasional),
	('/jadwal-recurve.html', JadwalRecurve.JadwalRecurve),
	('/jadwal-compound.html', JadwalCompound.JadwalCompound),
	('/hasil-nasional.html', HasilNasional.HasilNasional),
	('/hasil-recurve.html', HasilRecurve.HasilRecurve),
	('/hasil-compound.html', HasilCompound.HasilCompound),
	('/kontak.html', Kontak.Kontak),
    ('/admin/dashboard.html', Admin.Admin),
], debug=True)