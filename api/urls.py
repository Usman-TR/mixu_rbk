from django.urls import path
from api.views import RecognizedVideos, recognize_video

urlpatterns = [
    path('recognized_videos/', RecognizedVideos.as_view(), name='recognized_videos'),
    path('recognize_video/', recognize_video, name='recognize_video'),
]