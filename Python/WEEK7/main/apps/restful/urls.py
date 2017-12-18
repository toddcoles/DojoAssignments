from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^restful$', views.index),
    url(r'^restful/add_user$', views.add_user),
    url(r'^restful/add_person$', views.add_person),
    url(r'^restful/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^restful/(?P<user_id>\d+)/update$', views.update),
    url(r'^restful/(?P<user_id>\d+)/show$', views.show),
    url(r'^restful/(?P<user_id>\d+)/destroy$', views.delete)
]