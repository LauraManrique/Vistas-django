from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =[
    path('list/', views.get_measurements, name='measurementList')
]