from django.conf.urls import url
from rango import views

urlpatterns=[
    url(r'^$' , views.index , name='index'),
    url(r'^about/' , views.about , name='about'),
    url(r'^session/(?P<sessionid>.+)/$', views.startsession, name='chat_start'),
    url(r'^add_user/',views.add_user,name='add_user'), #comment it later 
]
