import webapp2
import jinja2
import os
from google.appengine.api import mail
import re

class Handler(webapp2.RequestHandler):

 	def initialize(self, *a, **kw):
		webapp2.RequestHandler.initialize(self, *a, **kw)
		self.template_dir = os.path.join(os.path.dirname(__file__), 'html')
		self.jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.template_dir), autoescape=True)
		# self.user_cookie_name = 'user_id'
		# uid = self.read_secure_cookie(self.user_cookie_name)
		# self.user = uid and User.get_by_id(int(uid))

	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = self.jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


	def set_secure_cookie(self, name, val, days = None):
		cookie_val = make_secure_val(str(val))
		if days == None:
			self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/' % (name, cookie_val))
		else:
			expiration = datetime.datetime.now() + datetime.timedelta(days = days)
			self.response.headers.add_header('Set-Cookie', '%s=%s; expires=%s; Path=/;' % (name, cookie_val, expiration.strftime("%a, %d-%b-%Y %H:%M:%S GMT")))


	def read_secure_cookie(self, name):
		cookie_val = self.request.cookies.get(name)
		if cookie_val and check_secure_val(cookie_val):
			return cookie_val.split('|')[0]

	def render_default_header(self):
		self.write(self.getDefaultHeader())
