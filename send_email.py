import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
	from_email='from_email@example.com',
	to_emails='nyiwende@gmail.com',
	subject='sending an email yeeiy',
	html_content='<strong>sending an email yeeiy</strong>')

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.send(message)
print(response.status_code, response.body, response.headers)

	