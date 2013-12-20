from Handler import *

class FrontHandler(Handler):
	def get(self):
		self.render("front.html")