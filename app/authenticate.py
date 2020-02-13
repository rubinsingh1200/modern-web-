from django.shortcuts import redirect,render
from app.models import User 
from django.db.models import Q 
from django.http import HttpResponse 
from django.contrib import messages


class Authenticate:
	def valid_user(function):
		def wrap (request):
			try:
				User.objects.get(Q(email=request.session["email"]) & Q(password=request.session['password']))
				return function(request)
			except:
				messages.warning(request,"User not found")
				return redirect('/login')
		return wrap

	def valid_user_with_id(function):
		def wrap (request,id):
			try:
				User.objects.get(email=request.session["email"]) & Q(password=request.session['password'])
				return function(request,id)
			except:
				messages.warning(request,"Please Login")
				return redirect('/login')
		return wrap
	

	def guest(function):
		def wrap(request):
			if 'email' not in request.session:
				return function(request)
			else:
				return redirect('/admin')
		return wrap	