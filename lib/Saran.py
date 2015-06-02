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

DEFAULT_BOX_NAME = 'kotakSaran'

# Box key
def box_key(box_name=DEFAULT_BOX_NAME):
    return ndb.Key('KotakSaran', box_name)

# Class Saran

class Saran(ndb.Model):
    nama = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=False)
    isi = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

    def listSaran(self):
        # Set variable name
        box_name = DEFAULT_BOX_NAME
        
        # Instantiates a query
        saran_query = Saran.query(ancestor=box_key(box_name)).order(+Saran.date)
        
        # Execute the query
        saran = saran_query.fetch(5)
        
        return saran
    
    def insertToDatastore(self, nama, email, isi):
        # Set variable name
        box_name = DEFAULT_BOX_NAME
        
        # Set datastore name
        saran = Saran(parent=box_key(box_name))
        
        # Input into model's attribute
        saran.nama = nama
        saran.email = email
        saran.isi = isi

        logging.info(saran.nama)

        # Submit
        saran.put()
    
    def deleteSaran(self, saranID):
        # Define variables
        box_name = DEFAULT_BOX_NAME
        
        # Get the post
        saranID = int(saranID)
        key = box_key(box_name)
        saran = Saran.get_by_id(saranID, parent=key)
        saran.key.delete()

    def getSaran(self, saranID):
        # Define variables
        box_name = DEFAULT_BOX_NAME

        # Get the post
        saranID = int(saranID)
        key = box_key(box_name)
        saran = Saran.get_by_id(saranID, parent=key)
        return saran