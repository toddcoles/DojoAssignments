from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/add_review$', views.add_review),
    url(r'^/create$', views.create),
    url(r'^/user/(?P<user_id>\d+)$', views.user),
    url(r'^/show/(?P<book_id>\d+)$', views.show)
    # url(r'^register$', views.register),
    # url(r'^login$', views.login),
    # url(r'^success$', views.success)
    # url(r'^course/(?P<course_id>\d+)/destroy$', views.delete)
    # url(r'^restful/(?P<user_id>\d+)/edit$', views.edit),
    # url(r'^restful/(?P<user_id>\d+)/update$', views.update),
    # url(r'^restful/(?P<user_id>\d+)/show$', views.show),
    # url(r'^restful/(?P<user_id>\d+)/destroy$', views.delete)
]