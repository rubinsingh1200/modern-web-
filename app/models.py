from django.db import models


class User(models.Model):
	user_id=models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	image=models.ImageField(default="img.jpg")
	class Meta:
		db_table="user"

class Categories(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	title=models.CharField(max_length=50)
	class Meta:
		db_table="categories"

class Posts(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	categories=models.ForeignKey(Categories,on_delete=models.CASCADE, null=True, default=None)
	title=models.TextField(blank= True)
	date=models.CharField(max_length=50)
	content=models.TextField(blank= True)
	author=models.CharField(max_length=50)
	image=models.ImageField(default="img.jpg")
	class Meta:
		db_table="posts"

class Horoscope(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=50)
	date=models.CharField(max_length=50)
	content=models.TextField(blank= True)
	image=models.ImageField(default="img.jpg")
	class Meta:
		db_table="horoscope"

class Advert(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	title=models.CharField(max_length=50)
	image=models.ImageField(default="img.jpg")
	class Meta:
		db_table="advert"





			


# Create your models here.

