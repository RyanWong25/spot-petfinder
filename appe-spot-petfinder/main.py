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


class SpottedPet(ndb.Model):
    lat = ndb.StringProperty()
    lng = ndb.StringProperty()


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render())

class LostMapPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/map.html')
        self.response.write(template.render())

# class LostLocationHandler(webapp2.RequestHandler):
#     #saves lost location entered by user
#     def post(self):
#         lost_location = self.request.get('lostLocation')
#         lost_location = json.loads(lost_location)
#         lat = str(lost_location['lat'])
#         lng = str(lost_location['lng'])
#
#
#     #returns all lost locations entered into database
#     def get(self):
#
# class SpotLocationHandler(webapp2.RequestHandler):
#     #saves spotted locations entered by users
#     def post(self):
#
#     #returns all spotted locations entered into database
#     def get(self):
#

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/lost', LostMapPage),
    # ('/postlost', LostLocationHandler),
    # ('/getlost', LostLocationHandler),
    # ('/postspot', SpotLocationHandler),
    # ('/getspot', SpotLocationHandler),
], debug=True)
