from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse
from django.core.mail import send_mail



from .forms import Contactform 



# Create your views here.
#def index(request):
	
   # return render(request, 'blog/index.html', {})
def index(request):
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			sender_name = request.POST['name']
			sent_email = request.POST['email']
			sender_message = request.POST['message']
			send_mail(sender_name, sender_message, [sent_email], ['nyiwendesally@gmail.com'], fail_silently=False)

		return render(request, 'blog/index.html', {'sender_name': sender_name})
	else:
		form = Contactform(request.POST)
	return render(request, 'blog/index.html', {'form': form})
