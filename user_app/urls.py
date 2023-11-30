from django.urls import path
from user_app import views


urlpatterns = [
    path('logout2/', views.logout2, name="logout2"),
    path('home/', views.home, name="home"),
    path('createuser/', views.createuser, name="createuser"),
    path('', views.login, name="login"),
    path('watchmovie1/<int:movieid>/', views.watchmovie1, name="watchmovie1"),
    path('music/', views.music, name="music"),
    path('showartist/', views.showartist, name="showartist"),
    path('showmoviess/', views.showmoviess, name="showmoviess"),
    path('hearsong1/<str:sngmovie>/', views.hearsong1, name="hearsong1"),
    path('hearsong2/<str:sngartist>/', views.hearsong2, name="hearsong2"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('watchlater/<int:mid>/', views.watchlater, name="watchlater"),
    path('watchlatershow/', views.watchlatershow, name="watchlatershow"),
    path('watchlaterremove/<int:mid>/', views.watchlaterremove, name="watchlaterremove"),
]