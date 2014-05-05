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
import webapp2

from Handler import *
from FrontHandler import *
from SamplesHandler import *
from ContactHandler import *
from FAQHandler import *
import re

class MainHandler(Handler):
    def get(self):
        self.response.write('Hello world!')

class ExperimentHandler(Handler):
	def get(self):
		self.render('experiment.html')

app = webapp2.WSGIApplication([
    ('/', FrontHandler),
    ('/samples', SamplesHandler),
    ('/contact', ContactHandler),
    ('/faq', FAQHandler),
    (r'/samples/([a-z0-9\w]+)', SamplesZoomHandler),
    ('/experimental', ExperimentHandler)
], debug=True)
