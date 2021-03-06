#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import jinja2
import os
import json
import webapp2
import random
import logging
from google.appengine.api import users
from google.appengine.ext import ndb


class LostPet(ndb.Model):
    lat = ndb.StringProperty()
    lng = ndb.StringProperty()
    name = ndb.StringProperty()
    pet = ndb.StringProperty()
    phone = ndb.StringProperty()
    misc = ndb.StringProperty()

# class SpotPet(ndb.Model):
#     lat = ndb.StringProperty()
#     lng = ndb.StringProperty()


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # template = jinja_environment.get_template('templates/form3.html')
        # self.response.write(template.render())

        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render())

        # my_vars = {
        #
        # "ownername" : self.request.get("ownername"),
        # "ownernum" : self.request.get("ownername"),
        # "petname" : self.request.get("petname"),
        # "lostpet" : self.request.get("lostpet"),
        # "breed" : self.request.get("breed"),
        # "height" : self.request.get("height"),
        # "weight" : self.request.get("weight"),
        # "misc" : self.request.get("misc")
        #
        # }

class LostPetHandler(webapp2.RequestHandler):
    def post(self):
        logging.info('got a request')

        """POST request handler, saves the new location into the database.
        A user can only have one row in the database, so multiple entries
        will overwrite each other."""

        # Make sure the user is signed in, because we need their identity
        # to save it along with the coordinates
            # Get the request data
        lat = self.request.get('lat')
        lng = self.request.get('lng')
        name = self.request.get('name')
        pet = self.request.get('pet')
        # name = json.loads(name)
        phone = self.request.get('phone')
        misc = self.request.get('misc')

        if lat and lng and name and pet and phone and misc:
            l = LostPet(lat = lat, lng = lng, name = name, pet = pet, phone = phone, misc = misc)
            l.put()
            logging.info('entered lost pet')
            # lat = str(location['lat'])
            # lng = str(location['lng'])
            # k = LostPet.query().get()
            # Let's first check if this user already exists in the database
            # If they do, get that entry (its key) and modify it
            # if k:
            #     instance = k
            #     instance.lat = lat
            #     instance.lng = lng
            # else:
                # instance = LostPet(name=user.nickname(), lat=lat, lng=lng)
            # instance.put()

    def get(self):
        q = LostPet.query()
        p = q.fetch()
        # Turn the list from a list of Birthplace objects into list of dicts
        result = [i.to_dict() for i in p]
        self.response.write(json.dumps(result))

class GetLostPetHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/alldogsmap.html')
        self.response.write(template.render())

class MarkLostPetHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/map.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/lost', LostPetHandler),
    ('/getlost', GetLostPetHandler),
    ('/marklost', MarkLostPetHandler),
], debug=True)
