"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add',views.addblog,name='add'),
    path('feedback',views.feed,name='feedback'),
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('search',views.search,name='search'),
    path('readmore<int:id>',views.read,name='readmore'),
    path('hollywood',views.hollywood,name='hollywood'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('chpass', views.change_password, name='change_password'),
    path('addprofile', views.add_profile_photo, name= 'add_profile_photo'),
    path('profile', views.profile, name= 'profile'),
    path('up/<int:id>', views.update_profile, name= 'update_profile'),
   



]