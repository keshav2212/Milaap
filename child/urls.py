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
    path('login/',views.login1,name='login'),
    path('addmember/',views.addmember,name='addmember'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout1,name='logout'),
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
    path('<int:memberid>',views.deletemember,name='deletemember')
]
