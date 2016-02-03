from srepo.views import BuildViewSet, ApplicationViewSet, api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url,include
from srepo import views

build_list = BuildViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
build_detail = BuildViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

application_list = ApplicationViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
application_detail = ApplicationViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^builds/$', build_list, name='build-list'),
    url(r'^builds/(?P<pk>[0-9]+)/$', build_detail, name='build-detail'),
    url(r'^applications/$', application_list, name='application-list'),
    url(r'^applications/(?P<pk>[a-z|0-9]{3})/$', application_detail, name='application-detail'),
    url(r'^applications/(?P<pk>[a-z|0-9]{3})/(?P<tag>.+)/$', views.ApplicationTagSearch.as_view()),
])