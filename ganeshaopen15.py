# Libraries used

import os
import cgi
import urllib
import logging

from datetime import datetime

# Public
from lib import TentangKami
from lib import JadwalNasional
from lib import JadwalRecurve
from lib import JadwalCompound
from lib import HasilNasional
from lib import HasilRecurve
from lib import HasilCompound
from lib import Kontak
from lib import Post

# Admin
from lib import PostController
from lib import Admin
from lib import LoginController
from lib import LogoutController
from lib import Registrasi
from lib import PostMenu
from lib import Galeri
from lib import KotakSaran

from pytz import timezone

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
            datetimeList.append(jkt_dt.strftime("%d-%m-%Y %H:%M:%S"))
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

# Routes
	
application = webapp2.WSGIApplication([
	('/', MainPage),
    ('/registrasi', Registrasi.Registrasi),
	('/tentang-kami', TentangKami.TentangKami),
	('/jadwal/nasional', JadwalNasional.JadwalNasional),
	('/jadwal/recurve', JadwalRecurve.JadwalRecurve),
	('/jadwal/compound', JadwalCompound.JadwalCompound),
	('/hasil/nasional', HasilNasional.HasilNasional),
	('/hasil/recurve', HasilRecurve.HasilRecurve),
	('/hasil/compound', HasilCompound.HasilCompound),
	('/kontak', Kontak.Kontak),
    ('/admin/dashboard', Admin.Admin),
    ('/admin/login', LoginController.LoginController),
    ('/admin/logout', LogoutController.LogoutController),
    ('/admin/post-menu', PostMenu.PostMenu),
    ('/admin/post', PostController.PostController),
    ('/admin/kotak-saran', KotakSaran.KotakSaran),
    ('/admin/galeri', Galeri.Galeri),
], debug=True)