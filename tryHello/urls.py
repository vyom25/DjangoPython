from django.urls import path
from .views import hello_world

urlpatterns = [path('hello/<str:name>', hello_world, name='hi')]
