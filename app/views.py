from django.shortcuts import render,redirect 
from app.models import User 
from app.models import Posts
from app.models import Categories
from app.models import Horoscope
from app.models import Advert
from app.forms import UserForm
from app.forms import NewsForm
from app.forms import HoForm
from app.forms import AForm
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from app.authenticate import Authenticate
from django.contrib import messages

#---------------------------------------for backend admin side -------------------------------------------------------------
def login(request):
	return render(request,'login.html')

def logout(request):
	request.session.flush()
	return redirect('/login')

@Authenticate.valid_user
def dashboard(request):
	u=len(User.objects.all())
	p=len(Posts.objects.all())
	a=len(Advert.objects.all())
	return render(request,'dashboard.html',{'u':u,'p':p,'a':a})



def entry(request):
	try:
		User.objects.get(email=request.POST['email'])
	except:
		
		messages.warning(request,"User not found")
		return redirect('/login')
	request.session['email']=request.POST['email']
	request.session['password']=request.POST['password']
	return redirect("/admin")


# ------------------------------------------ for users------------------------------------------------------------------
@Authenticate.valid_user
def usersIndex(request):
	page=1
	if request.method=="POST":
		limit=5
		if 'prev' in request.POST:
			page=(int(request.POST['page']) -1)
		else:
			page=(int(request.POST['page']) +1)
		tempoffset=page-1
		offset=0
		if tempoffset > 0:
			offset=tempoffset * limit
		users =User.objects.raw("select * from user limit 5 offset %s",[offset])
	else:
		users =User.objects.raw("select * from user limit 5 offset 0")
	count=User.objects.count()
	return render(request,"users/index.html",{'users':users,'counts':count,'page':page})

@Authenticate.valid_user
def usersCreate(request):
	if request.method=="POST":
		form=UserForm(request.POST,request.FILES)
		form.save()
		return redirect('/users')
		
	form=UserForm()
	return render(request,'users/create.html',{'form':form})

# @Authenticate.valid_user
def usersEdit(request,id):
	user=User.objects.get(user_id=id)
	return render(request,'users/edit.html',{'user':user})

# @Authenticate.valid_user
def usersUpdate(request,id):
	user=User.objects.get(user_id=id)
	form=UserForm(request.POST,request.FILES,instance=user)
	form.save()
	return redirect('/users')


def usersDelete(request,id):
	user=User.objects.get(user_id=id)
	if(user.image!='img.jpg'):
		user.image.delete()
	user.delete()
	return redirect('/users')

def search(request):
	users=User.objects.filter(email__contains=request.GET['search']).values()
	return JsonResponse(list(users),safe=False)


# ----------------------------------------for news--------------------------------------------------------------- 
@Authenticate.valid_user
def newsIndex(request):
	page=1
	if request.method=="POST":
		limit=5
		if 'prev' in request.POST:
			page=(int(request.POST['page']) -1)
		else:
			page=(int(request.POST['page']) +1)
		tempoffset=page-1
		offset=0
		if tempoffset > 0:
			offset=tempoffset * limit
		news =Posts.objects.raw("select * from  posts order by id desc limit 5 offset %s",[offset])
	else:
		news =Posts.objects.raw("select * from posts order by id desc limit 5 offset 0")
	count=Posts.objects.count()
	return render(request,"news/index.html",{'news':news,'counts':count,'page':page})

@Authenticate.valid_user
def newsCreate(request):
	if request.method=="POST":
		form=NewsForm(request.POST,request.FILES)
		form.save()
		return redirect('/news')
		
	form=NewsForm()
	categories = Categories.objects.all()
	return render(request,'news/create.html',{'form':form, 'categories': categories})


def newsEdit(request,id):
	news=Posts.objects.get(id=id)
	categories = Categories.objects.all()
	return render(request,'news/edit.html',{'news':news,'categories':categories})

# @Authenticate.valid_user_with_id
def newsUpdate(request,id):
	news=Posts.objects.get(id=id)
	form=NewsForm(request.POST,request.FILES,instance=news)
	form.save()
	return redirect('/news')


def newsDelete(request,id):
	news=Posts.objects.get(id=id)
	if(news.image!='img.jpg'):
		news.image.delete()
	news.delete()
	return redirect('/news')





#  -----------------------------------------for horoscope------------------------------------------------------------
@Authenticate.valid_user
def hoIndex(request):
	page=1
	if request.method=="POST":
		limit=6
		if 'prev' in request.POST:
			page=(int(request.POST['page']) -1)
		else:
			page=(int(request.POST['page']) +1)
		tempoffset=page-1
		offset=0
		if tempoffset > 0:
			offset=tempoffset * limit
		horoscope =Horoscope.objects.raw("select * from horoscope order by id desc limit 6 offset %s",[offset])
	else:
		horoscope =Horoscope.objects.raw("select * from horoscope order by id desc limit 6 offset 0")
	count=Posts.objects.count()
	return render(request,"horoscope/index.html",{'horoscope':horoscope,'counts':count,'page':page})

@Authenticate.valid_user
def hoCreate(request):
	if request.method=="POST":
		form=HoForm(request.POST,request.FILES)
		form.save()
		return redirect('/horoscope')
		
	form=HoForm()
	return render(request,'horoscope/create.html',{'form':form})


def hoEdit(request,id):
	horoscope=Horoscope.objects.get(id=id)
	return render(request,'horoscope/edit.html',{'horoscope':horoscope})

@Authenticate.valid_user_with_id
def hoUpdate(request,id):
	horoscope=Horoscope.objects.get(id=id)
	form=HoForm(request.POST,request.FILES,instance=horoscope)
	form.save()
	return redirect('/horoscope')


def hoDelete(request,id):
	horoscope=Horoscope.objects.get(id=id)
	if(horoscope.image!='img.jpg'):
		horoscope.image.delete()
	horoscope.delete()
	return redirect('/horoscope')

def horsearch(request):
	horoscope=Horoscope.objects.filter(name__icontains=request.GET['search']).values()
	return JsonResponse(list(horoscope),safe=False)


#--------------------------------------for advertisement--------------------------------------------------------
@Authenticate.valid_user
def aIndex(request):
	page=1
	if request.method=="POST":
		limit=6
		if 'prev' in request.POST:
			page=(int(request.POST['page']) -1)
		else:
			page=(int(request.POST['page']) +1)
		tempoffset=page-1
		offset=0
		if tempoffset > 0:
			offset=tempoffset * limit
		advert = Advert.objects.raw("select * from advert order by id desc limit 6 offset %s",[offset])
	else:
		advert = Advert.objects.raw("select * from advert order by id desc limit 6 offset 0")
	count=Posts.objects.count()
	return render(request,"advert/index.html",{'advert':advert,'counts':count,'page':page})

@Authenticate.valid_user
def aCreate(request):
	if request.method=="POST":
		form=AForm(request.POST,request.FILES)
		form.save()
		return redirect('/advert')
		
	form=AForm()
	return render(request,'advert/create.html',{'form':form})


def aEdit(request,id):
	advert=Advert.objects.get(id=id)
	return render(request,'advert/edit.html',{'advert':advert})

@Authenticate.valid_user_with_id
def aUpdate(request,id):
	advert=Advert.objects.get(id=id)
	form=AForm(request.POST,request.FILES,instance=advert)
	form.save()
	return redirect('/advert')


def aDelete(request,id):
	advert=Advert.objects.get(id=id)
	if(advert.image!='img.jpg'):
		advert.image.delete()
	advert.delete()
	return redirect('/advert')

# -------------------------------------------------------------------------------------------------------------------

#---------------------------------------------for frontend----------------------------------------------------------
def homePage(request):
	categories = Categories.objects.all()
	posts=Posts.objects.all()
	advert=Advert.objects.all()
	request.session.flush()
	return render(request,'frontend/index.html',{'posts':posts,'categories': categories, 'advert':advert})

def fContact(request):	
	categories = Categories.objects.all()
	return render(request,'frontend/contact.html',{'categories': categories})

def fAboutus(request):
	categories = Categories.objects.all()
	return render(request, 'frontend/about.html',{'categories': categories})

def fPrivacy(request):
	categories = Categories.objects.all()
	return render(request, 'frontend/privacy.html',{'categories': categories})

def fHoroscope(request):
	horoscope = Horoscope.objects.all()
	categories = Categories.objects.all()
	return render(request, 'frontend/horoscope.html',{'horoscope': horoscope,'categories': categories})

def postView(request,id):
	news=Posts.objects.filter(id=id)
	categories = Categories.objects.all()
	return render(request,'frontend/single-post.html',{'news':news,'categories':categories})

def hpostView(request,id):
	horoscope=Horoscope.objects.filter(id=id)
	categories = Categories.objects.all()
	return render(request,'frontend/hsingle-post.html',{'horoscope':horoscope,'categories':categories})

def categoryView(request,id):
	category=Categories.objects.filter(id=id)
	categories = Categories.objects.all()
	return render(request,'frontend/category-page.html',{'categories':categories, 'category':category.first()})