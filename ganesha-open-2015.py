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
        Post = Blog.Blog()
        posts = Post.listPosts()
        returnString = ""
        
        # Timezone convertion
        # Set timezone
        jkt = timezone('Asia/Jakarta')
        utc = timezone('UTC')
        
        # For post in posts ...
        for post in posts:
            title = post.title
            content = post.content
            
            # Convert timezone
            utc_dt = utc.localize(post.date)
            jkt_dt = utc_dt.astimezone(jkt)
            
            # Write to time
            time = jkt_dt
            
            # Hard-coded HTML page
            returnString = returnString + "<div class=\"col-md-8\">" + title + "</div>" + "<br>"
        
		# Loads the page
        template_values = {
            'returnString': returnString,
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