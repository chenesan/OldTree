from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^answer/$', views.answer, name='answer'),
    url(r'^your_tree/$', views.your_tree, name='your_tree'),
    url(r'^message/$', views.message, name='message'),
    url(r'^send_message/$', views.send_message, name='send_message'),
]
