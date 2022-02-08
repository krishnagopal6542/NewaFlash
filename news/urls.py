from django.urls import path
from . import views


urlpatterns = [
    path("",views.news_flash,name='news_flash'),
]
