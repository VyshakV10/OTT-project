from django.urls import path
from admin_app import views

urlpatterns = [
    path('adminpg/', views.adminpg, name="adminpg"),
    path('addmovie/', views.addmovie, name="addmovie"),
    path('movieshow/', views.movieshow, name="movieshow"),
    path('movieshow1/', views.movieshow1, name="movieshow1"),
    path('movieshow2/', views.movieshow2, name="movieshow2"),
    path('editmovies/<int:movieid>/', views.editmovies, name="editmovies"),
    path('updatemovie/<int:movieid>/', views.updatemovie, name="updatemovie"),
    path('deletemovie/<int:movieid>/', views.deletemovie, name="deletemovie"),
    path('addsong/', views.addsong, name="addsong"),
    path('songshow/', views.songshow, name="songshow"),
    path('songshow1/', views.songshow1, name="songshow1"),
    path('editsongs/<int:songid>/', views.editsongs, name="editsongs"),
    path('updatesong/<int:songid>/', views.updatesong, name="updatesong"),
    path('deletesong/<int:songid>/', views.deletesong, name="deletesong"),
    path('watchmovie/<int:movieid>/', views.watchmovie, name="watchmovie"),
    path('addactors/<int:movieid>/', views.addactors, name="addactors"),
    path('viewactors/<int:movieid>/', views.viewactors, name="viewactors"),
    path('addactors1/', views.addactors1, name="addactors1"),
    path('logout/', views.logout, name="logout"),
]