from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from . import views
from django.shortcuts import render


urlpatterns = [
    path('', views.index, name='index'), #path 함수를 통해 index함수를 실행시킬 urlpattern을 정의하고 이러한 urlpattern을 index라는 이름으로 부르겠다고 선언해준 것입니다.
    #path('catalog/<int:id>',views.update,name='edit'),
    #path('detail/<int:person_id>/edit', views.edit, name='edit'),
]
