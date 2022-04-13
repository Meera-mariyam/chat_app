from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('<str:username>/',chatPage,name='chat')
]
