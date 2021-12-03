from rest_framework import  generics
from recognize_videos.models import RecognizeVideo
from api.serializers import RecognizeVideoSerializer
from neural.tools import create_audio, transcribe
class RecognizedVideos(generics.ListCreateAPIView):
    queryset = RecognizeVideo.objects.all()
    serializer_class = RecognizeVideoSerializer


def recognize_video(request, video):
    audio = create_audio(video)
    recognize_audio = transcribe(audio)
    print(recognize_audio)
    print(True)