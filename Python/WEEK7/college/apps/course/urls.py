from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^course/add_course$', views.add_course),
    url(r'^course/(?P<course_id>\d+)/destroy$', views.delete)
    # url(r'^restful/(?P<user_id>\d+)/edit$', views.edit),
    # url(r'^restful/(?P<user_id>\d+)/update$', views.update),
    # url(r'^restful/(?P<user_id>\d+)/show$', views.show),
    # url(r'^restful/(?P<user_id>\d+)/destroy$', views.delete)
]