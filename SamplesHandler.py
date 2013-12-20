from Handler import *

class SamplesHandler(Handler):
	def get(self):
		self.render('samples.html')


class SamplesZoomHandler(Handler):
	def get(self, pic):
		self.write("""<img src="../res/%s.png" width="600px">""" % pic)