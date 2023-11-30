from django.shortcuts import render,redirect
from django.http import *
from django.template import RequestContext
from admin_app.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



def adminpg(request):
    return render(request, 'admin.html')



def addmovie(request):
    if request.method == "POST":
        moviename=request.POST['moviename']
        moviecategory=request.POST['moviecategory']
        moviedirector=request.POST['moviedirector']
        imdbrating=request.POST['imdbrating']
        moviedisciption=request.POST['moviedisciption']
        movieposter=request.FILES['movieposter']
        movievideo=request.FILES['movievideo']

        data=Movies(
            moviename=moviename,
            moviecategory=moviecategory,
            moviedirector=moviedirector,
            imdbrating=imdbrating,
            moviedisciption=moviedisciption,
            movieposter=movieposter,
            movievideo=movievideo, 
        )
        data.save()
    return render(request, 'addmovies.html')



def movieshow(request):
    moviedetail=Movies.objects.all()
    context={
        'moviedetail' : moviedetail
    }
    return render(request , 'viewmovies.html' , context)


def movieshow1(request):
    moviedetail=Movies.objects.all()
    context={
        'moviedetail' : moviedetail
    }
    return render(request , 'editmovies.html' , context)



def movieshow2(request):
    moviedetail=Movies.objects.all()
    context={
        'moviedetail' : moviedetail
    }
    return render(request , 'movieview.html' , context)



def viewactors(request, movieid):
    actordetail=Actors.objects.filter(movieid=movieid) 
    return render(request, 'viewactor.html', {'actordetail' : actordetail , 'movieid' : movieid})



def editmovies(request, movieid):
    moviedetail=Movies.objects.filter(id=movieid) 
    return render(request, 'updatemovie.html', {'moviedetail' : moviedetail , 'movieid' : movieid})



def updatemovie(request, movieid):
    if request.method == "POST":
        moviename=request.POST['moviename']
        moviecategory=request.POST['moviecategory']
        moviedirector=request.POST['moviedirector']
        imdbrating=request.POST['imdbrating']
        moviedisciption=request.POST['moviedisciption']
        try:
            movieposter=request.FILES['movieposter']
            fs=FileSystemStorage()
            file=fs.save(movieposter.name,movieposter)

        except MultiValueDictKeyError:
            file=Movies.objects.get(id=movieid).movieposter
             

        Movies.objects.filter(id=movieid).update(
             
            moviename=moviename,
            moviecategory=moviecategory,
            moviedirector=moviedirector,
            imdbrating=imdbrating,
            moviedisciption=moviedisciption,
            movieposter=file, 
        )
        return redirect('movieshow1')
    return render(request,'editmovies.html')




def deletemovie(request, movieid):
    movie=Movies.objects.get(id=movieid)
    movie.delete()
    return redirect('movieshow1')




def addsong(request):
    if request.method == "POST":
        songname=request.POST['songname']
        songcategory=request.POST['songcategory']
        songartist=request.POST['songartist']
        songmovie=request.POST['songmovie']
        songposter=request.FILES['songposter']
        song=request.FILES['song']

        data=Songs(
            songname=songname,
            songcategory=songcategory,
            songartist=songartist,
            songmovie=songmovie,
            songposter=songposter,
            song=song, 
        )
        data2=Smovies(
            songmovie=songmovie,
        )
        data3=Artist(
            songartist=songartist,
        )
        data.save()
        data2.save()
        data3.save()
    return render(request, 'addsongs.html')



def songshow(request):
    songdetail=Songs.objects.all()
    context={
        'songdetail' : songdetail
    }
    return render(request , 'viewsongs.html' , context)


def songshow1(request):
    songdetail=Songs.objects.all()
    context={
        'songdetail' : songdetail
    }
    return render(request , 'editsongs.html' , context)



def editsongs(request, songid):
    songdetail=Songs.objects.filter(id=songid) 
    return render(request, 'updatesong.html', {'songdetail' : songdetail , 'songid' : songid})




def updatesong(request, songid):
    if request.method == "POST":
        songname=request.POST['songname']
        songcategory=request.POST['songcategory']
        songartist=request.POST['songartist']
        songmovie=request.POST['songmovie']
        try:
            songposter=request.FILES['songposter']
            fs=FileSystemStorage()
            file=fs.save(songposter.name,songposter)

        except MultiValueDictKeyError:
            file=Songs.objects.get(id=songid).songposter
             

        Songs.objects.filter(id=songid).update(
             
            songname=songname,
            songcategory=songcategory,
            songartist=songartist,
            songmovie=songmovie,
            songposter=file, 
        )
        return redirect('songshow1')
    return render(request,'editsongs.html')


def deletesong(request,songid):
    song=Songs.objects.get(id=songid)
    song.delete()
    return redirect('songshow1')


def watchmovie(request, movieid):
    moviedetail=Movies.objects.filter(id=movieid) 
    return render(request, 'video.html', {'moviedetail' : moviedetail , 'movieid' : movieid})





def addactors(request, movieid):
    if request.method == "POST":
        actorname=request.POST['actorname']
        actorphoto=request.FILES['actorphoto']

        data=Actors(
            actorname=actorname,
            actorphoto=actorphoto, 
            movieid=movieid
        )
        data.save()
    return render(request, 'addactors.html')



def addactors1(request):
    return redirect(request, 'movieshow2.html')



def login(request):
    return render(request, 'login.html')


def home(request):
    moviedetail=Movies.objects.all()
    context={
        'moviedetail' : moviedetail
    }
    return render(request, 'homepg.html', context)



def logout(request):
    del request.session['name'],request.session['email'],request.session['phone'],request.session['id']
    return redirect('login')
