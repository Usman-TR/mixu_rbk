from django.urls import path
from api.views import RecognizedVideos

urlpatterns = [
    path('recognized_videos/', RecognizedVideos.as_view(), name='recognized_videos')
]