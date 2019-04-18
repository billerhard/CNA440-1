from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'polls/', views.polls, name='polls'),
    url(r'^bootstrap/', views.bootstrap, name='bootstrap'),
]