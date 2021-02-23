"""fithub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from exercises.views import (home_view, ex_detail_view, ex_list_view, search_view)

from post.views import post_create_view, post_list_view

from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('exercises/detail/<int:ex_id>', ex_detail_view),
    path('exercises', ex_list_view),
    path('search/<str:section>', search_view),
    path('create-post', post_create_view),
    path('posts', post_list_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),


]

urlpatterns += staticfiles_urlpatterns()