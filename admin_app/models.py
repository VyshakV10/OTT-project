from django.db import models

from OttProject import settings

# Create your models here.

class users(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    password=models.IntegerField()
    confirmpassword=models.IntegerField()
    type=models.CharField(max_length=10)
    subscription=models.CharField(max_length=10)
    profilephoto=models.ImageField(upload_to='movies', default="null.jpeg")

 
class Movies(models.Model):
    moviename=models.CharField(max_length=30)
    moviedisciption=models.CharField(max_length=150)
    moviecategory=models.CharField(max_length=20)
    movieposter=models.ImageField(upload_to='movies', default="null.jpeg")
    movievideo=models.FileField(upload_to='movies' , default="null.mp4")
    imdbrating=models.FloatField(default=0)
    moviedirector=models.CharField(max_length=30 , default="null") 
    

class Songs(models.Model):
    songname=models.CharField(max_length=30)
    songmovie=models.CharField(max_length=150)
    songcategory=models.CharField(max_length=20)
    songartist=models.CharField(max_length=200)
    songposter=models.ImageField(upload_to='movies', default="null.jpeg")
    song=models.FileField(upload_to='movies', default="null.mp3")



class Actors(models.Model):
    movieid=models.IntegerField()
    actorname=models.CharField(max_length=30)
    actorphoto=models.ImageField(upload_to='movies', default="null.jpeg")



class Smovies(models.Model):
    songmovie=models.CharField(max_length=30)


class Artist(models.Model):
    songartist=models.CharField(max_length=30)


class Watchlater(models.Model):
    userid=models.ForeignKey(users, on_delete=models.CASCADE)
    movieid=models.ForeignKey(Movies, on_delete=models.CASCADE)


