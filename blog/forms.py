from django import forms

class Contactform(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField(widget=forms.EmailInput)
	message = forms.CharField(widget=forms.Textarea)
	

	
