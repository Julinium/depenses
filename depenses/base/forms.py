from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Account

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class AccountForm(ModelForm):
	class Meta:
		model = Account
		exclude = ["user"]

	# def save(self, commit=True):
	# 	account = super(AccountForm, self).save(commit=False)
	# 	# account.user = request.user# self.cleaned_data['user']
	# 	if commit:
	# 		account.save()
	# 	return account