from django.urls import path
from api.views import VideosList, VideoRecognize

urlpatterns = [
    path('videos_list/', VideosList.as_view(), name='videos_list'),
    path('video_recognize/', VideoRecognize.as_view(), name='video_recognize'),
]