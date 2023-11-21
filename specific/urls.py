from specific.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('sql/',sql,name='sql'),
    path('web/',web,name='web'),
]