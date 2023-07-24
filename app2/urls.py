from django.urls import path
app_name='something'
from app2.views import *

urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]