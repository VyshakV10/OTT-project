from django.shortcuts import render,redirect
from django.http import *
from django.template import RequestContext
from admin_app.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

# Create your views here.
def home(request):
    if 'id' in request.session:
        moviedetail=Movies.objects.all()
        context={
            'moviedetail' : moviedetail
            }
        return render(request, 'homepg.html', context)
    else:
        return render(request,'login.html')






def watchmovie1(request,movieid):
    moviedetail=Movies.objects.filter(id=movieid)
    actordetail=Actors.objects.filter(movieid=movieid) 
    return render(request, 'watchmovies.html', {'moviedetail' : moviedetail , 'actordetail' : actordetail , 'movieid' : movieid})


def createuser(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        profilephoto=request.FILES['profilephoto']

        data=users(
            name=name,
            email=email,
            phone=phone,
            password=password,
            confirmpassword=confirmpassword,
            profilephoto=profilephoto,
            type="user" 
        )
        data.save()
    return render(request, 'createuser.html')



def login(request):
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        user="user"
        admin="admin"

        if users.objects.filter(name=name,password=password,type=user).exists():
            data=users.objects.filter(name=name,password=password).values('email','phone','id','profilephoto').first()
            request.session['name']=name
            request.session['email']=data['email']
            request.session['phone']=data['phone']
            request.session['id']=data['id']
            request.session['profilephoto']=data['profilephoto']
            return redirect('home')
        elif users.objects.filter(name=name,password=password,type=admin).exists():
            data=users.objects.filter(name=name,password=password).values('email','phone','id','profilephoto').first()
            request.session['name']=name
            request.session['email']=data['email']
            request.session['phone']=data['phone']
            request.session['id']=data['id']
            request.session['profilephoto']=data['profilephoto']
            return redirect('adminpg')
        else:
            return redirect('login')
    return render(request , 'login.html')



def music(request):
    songdetail=Songs.objects.all()
    context={
        'songdetail' : songdetail
    }
    return render(request, 'musicplayers.html', context)



def hearsong(request,songid):
    songdetail=Songs.objects.filter(id=songid)
    return render(request, 'musicplayers.html', {'songdetail' : songdetail , 'songid' : songid})


def showmoviess(request):
    all_objects = Smovies.objects.all()

    unique_values = set()

    duplicates = []

    for obj in all_objects:
        if obj.songmovie in unique_values:
            duplicates.append(obj)
        else:
            unique_values.add(obj.songmovie)
    for duplicate in duplicates:
        duplicate.delete()

    songmovied=Smovies.objects.all()
    context={
        'songmovied' : songmovied
    }
    return render(request, 'music.html', context)



def showartist(request):
    all_objects = Artist.objects.all()

    unique_values = set()

    duplicates = []

    for obj in all_objects:
        if obj.songartist in unique_values:
            duplicates.append(obj)
        else:
            unique_values.add(obj.songartist)
    for duplicate in duplicates:
        duplicate.delete()

    songartist=Artist.objects.all()
    context={
        'songartist' : songartist
    }
    return render(request, 'music2.html', context)



def hearsong1(request,sngmovie):
    songdetail=Songs.objects.filter(songmovie=sngmovie)
    return render(request, 'musicplayers.html', {'songdetail' : songdetail , 'sngmovie' : sngmovie})



def hearsong2(request,sngartist):
    songdetail=Songs.objects.filter(songartist=sngartist)
    return render(request, 'musicplayers.html', {'songdetail' : songdetail , 'sngartist' : sngartist})



def aboutus(request):
    return render(request, 'about.html')


def logout2(request):
    del request.session['name'],request.session['email'],request.session['phone'],request.session['id']
    return redirect('login')
    

def watchlater(request,mid):
    if 'id' in request.session:
        movieid=mid
        userid=request.session['id']
        if Watchlater.objects.filter(userid=userid,movieid=movieid).exists():
            return redirect('watchlatershow')
        else:
            data=Watchlater(
            movieid=Movies.objects.get(id=movieid),
            userid=users.objects.get(id=userid)
            )
            data.save()
        return redirect('home')
    return render(request, 'homepg.html')



def watchlatershow(request):
    userid=request.session['id']
    mvdetails=Watchlater.objects.filter(userid=userid)
    return render(request, 'watchlater.html', {'mvdetails' : mvdetails})


def watchlaterremove(request, mid):
    if 'id' in request.session:
        movie=Watchlater.objects.get(id=mid)
        movie.delete()
        return redirect('watchlatershow')
    return render(request, 'watchlater.html')