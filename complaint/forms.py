from django import forms
from django.forms import ModelForm

from .models import *


class updateForm(forms.ModelForm):
	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'edit current task...'}))
	desc = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'edit current task...'}))
	class Meta:
		model = Complaint
		fields = ['title' ,'desc']

class ComplaintForm(forms.ModelForm):
	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new complaint...'}))
	desc = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'enter description...'}))
	class Meta:
		model = Complaint
		fields = ['title' ,'desc']
