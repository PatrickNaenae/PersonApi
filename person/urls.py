from django.urls import path, re_path
from person.views import PersonViewSet

urlpatterns = [
    path('api/', PersonViewSet.as_view({'get': 'list', 'post': 'create'}), name='person-list'),
    re_path(r'^(?P<pk>\d+)/$', PersonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='person-detail'),
    re_path(r'^api/(?P<name>[^/]+)/$', PersonViewSet.as_view({'get': 'retrieve_by_name', 'put': 'update_by_name', 'delete': 'destroy_by_name'}), name='person-detail-by-name'),
]
