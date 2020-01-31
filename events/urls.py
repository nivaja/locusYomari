from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('events',views.event, name='events'),
    path('create_event', views.create_event, name='create_event'),
    path('join_chat', views.join_chat, name='join_chat'),
    path('search', views.search, name='search'),

]