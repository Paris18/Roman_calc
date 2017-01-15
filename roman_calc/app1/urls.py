from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^result',views.roman_clc, name = "calci" ),
]
