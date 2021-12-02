from rest_framework import  generics
from recognize_videos.models import RecognizeVideo
from .serializers import RecognizeVideoSerializer

class RecognizedVideos(generics.ListCreateAPIView):
    queryset = RecognizeVideo.objects.all()
    serializer_class = RecognizeVideoSerializer
