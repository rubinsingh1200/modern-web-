"""newsportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('',views.homePage),
    path('admin',views.dashboard),
# user urls
    path('users',views.usersIndex),
    path('users/create',views.usersCreate),
    path('users/edit/<int:id>',views.usersEdit),
    path('users/update/<int:id>',views.usersUpdate),
    path('users/delete/<int:id>',views.usersDelete),
    path('search',views.search),

# news posts urls
    path('news',views.newsIndex),
    path('news/create',views.newsCreate),
    path('news/edit/<int:id>',views.newsEdit),
    path('news/update/<int:id>',views.newsUpdate),
    path('news/delete/<int:id>',views.newsDelete),
    

# news horoscope urls
    path('horoscope',views.hoIndex),
    path('horoscope/create',views.hoCreate),
    path('horoscope/edit/<int:id>',views.hoEdit),
    path('horoscope/update/<int:id>',views.hoUpdate),
    path('horoscope/delete/<int:id>',views.hoDelete),
    path('horoscope/search',views.horsearch),

    
# news advertisement urls
    path('advert',views.aIndex),
    path('advert/create',views.aCreate),
    path('advert/edit/<int:id>',views.aEdit),
    path('advert/update/<int:id>',views.aUpdate),
    path('advert/delete/<int:id>',views.aDelete),

# authentication
    path('logout',views.logout),
    path('entry',views.entry),
    path('login',views.login),

 # frontend
    path('frontend/contact',views.fContact),
    path('frontend/privacy',views.fPrivacy),
    path('frontend/about-us',views.fAboutus),
    path('frontend/horoscope',views.fHoroscope),
    path('frontend/post/<int:id>',views.postView),
    path('frontend/hpost/<int:id>',views.hpostView),
    path('frontend/category/<int:id>',views.categoryView),

]

