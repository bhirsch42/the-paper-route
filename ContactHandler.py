from Handler import *

class ContactHandler(Handler):
	def get(self):
		self.render('contact.html')

	def post(self):
		name = self.request.get('name')
		email = self.request.get('email')
		confirm_email = self.request.get('confirm_email')
		project = self.request.get('project_type')
		reference = self.request.get('reference')
		details = self.request.get('details')

		# check form for errors
		name_blank = False
		email_mismatch = False
		project_type_blank = False
		email_error = False

		if '@' in email and '.' in email:
			email_error = False
		else:
			email_error = True
		if not name:
			name_blank = True
		if email != confirm_email:
			email_mismatch = True
		if not project:
			project_type_blank = True

		any_errors = name_blank or email_mismatch or project_type_blank or email_error

		if any_errors:
			self.render('contact.html', email_error=email_error, name_blank=name_blank, email_mismatch=email_mismatch, project_blank=project_type_blank,
				name=name, email=email, confirm_email=confirm_email, project=project, reference=reference, details=details)
		else:
			message = """

			Client name: %s 

			Client email: %s

			Project type: %s

			How they heard about The Paper Route: %s

			Project details: %s

			""" % (name, email, project, reference, details)

			mail.send_mail(sender="%s <%s>" % (name, email),
              to="Ellen Hirsch <benhirsch42@gmail.com>",
              subject="Paper Route Website email: %s" % project,
              body=message)
			self.write("Message sent.")
