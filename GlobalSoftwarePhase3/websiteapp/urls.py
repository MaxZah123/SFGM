from django.urls import path

from websiteapp.views import *

app_name = 'website'
urlpatterns = [
    path('index', index, name='index'),
    path('testlang', testlang, name='testlang'),
]

