from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^start/$', views.start),
    url(r'^answer/$', views.answer),
    url(r'^your_tree/$', views.your_tree, name='your_tree')
]
