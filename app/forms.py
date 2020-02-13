from django import forms
from app.models import User
from app.models import Posts
from app.models import Horoscope
from app.models import Advert

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields="__all__"

class NewsForm(forms.ModelForm):
	class Meta:
		model=Posts
		fields="__all__"

class HoForm(forms.ModelForm):
	class Meta:
		model=Horoscope
		fields="__all__"

class AForm(forms.ModelForm):
	class Meta:
		model=Advert
		fields="__all__"

