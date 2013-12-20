from Handler import *

class FAQHandler(Handler):
	def get(self):
		self.render('faq.html')