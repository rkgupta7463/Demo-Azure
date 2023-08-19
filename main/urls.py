from django.urls import path
from .views import index,home

urlpatterns = [
    path('',index, name='index'),
    path('my-intro/',home, name='home'),
]

