from django.urls import re_path
from .views import FaceMatchingViewSet
from . import views

urlpatterns = [
    #  Get matches for encoded 
    re_path(r'^face-matching/upload/$', FaceMatchingViewSet.as_view({'post': 'get_upload_matches'}), name='FaceMatchesList'),
]