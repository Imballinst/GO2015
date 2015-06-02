# Libraries used

import os
import cgi
import urllib
import logging

from google.appengine.ext import ndb
from pytz import timezone

import Saran
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

# Class KotakSaran    

class KotakSaran(webapp2.RequestHandler):
    def get(self):
        # Cookie check
        exp = self.request.cookies.get('expire')
        logging.info(exp)

        if (exp != None):
            valid = CookieManager.checkCookie(exp)
        else:
            valid = 0

        # Define variables
        saranObject = Saran.Saran()
        listSaran2 = saranObject.listSaran()
        count = len(listSaran2)
        
        # List
        saranIDList = []
        nameList = []
        emailList = []
        contentList = []
        datetimeList = []
        
        # Timezone convertion
        # Set timezone
        jkt = timezone('Asia/Jakarta')
        utc = timezone('UTC')

        # For post in posts ...
        for saran in listSaran2:
            # Convert timezone
            utc_dt = utc.localize(saran.date)
            jkt_dt = utc_dt.astimezone(jkt)

            content = saran.isi
            
            if (len(content) > 50):
                content = content[:50] + "..."

            # Insert to list
            nameList.append(saran.nama)
            emailList.append(saran.email)
            contentList.append(content)
            datetimeList.append(jkt_dt.strftime("%d-%m-%Y %H:%M:%S"))
            saranIDList.append(saran.key.id())

        # Loads the page
        template_values = {
            'valid': valid,
            'count': count,
            'nameList': nameList,
            'emailList': emailList,
            'contentList': contentList,
            'datetimeList': datetimeList,
            'saranIDList': saranIDList,
        }
        
        template = JINJA_ENVIRONMENT.get_template('/admin/kotak-saran.html')
        self.response.write(template.render(template_values))