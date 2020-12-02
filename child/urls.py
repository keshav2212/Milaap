from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import (
    LoginView, LogoutView
    )
from . import views
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name="home"),
    path('login/',LoginView.as_view(template_name='child/login.html'),name='login'),
    path('addmember/',views.addmember,name='addmember'),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('howitworks/',views.howitworks,name="howitworks"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',LogoutView.as_view(template_name='child/logout.html'),name='logout'),
    path('register/',views.register,name='register'),
    path('allmembers/',views.allmembers,name='allmembers'),
    path('laststep/',views.laststep),
    path('congrats/',views.congrats),
    path('search/',views.searchmember,name='search'),
    path('searchresult/',views.searchresult),
    path('addtolost/<int:id>',views.addtolost,name='addtolost'),
    path('deletefromlost/<int:id>',views.deletefromlost,name='deletefromlost'),
    url(r'^activate/<slug:uidb64>/<slug:token>/(?P<year>[0-9]{1,10})/$',views.activate, name='activate'),
    path('childdetails/',views.childdetails),
]
