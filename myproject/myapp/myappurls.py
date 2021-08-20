# In this python file we create the URLs for myapp

from django.conf.urls import url
from . import views     # from current directory import views

# list name "urlpatterns" is predefined so same name
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test', views.test, name='test'),
]
