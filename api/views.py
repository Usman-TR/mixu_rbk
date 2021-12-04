from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from rest_framework import  generics
from recognize_videos.models import RecognizeVideo
from api.serializers import VideosListSerializer, VideoRecognizeSerializer

class VideosList(generics.ListCreateAPIView):
    queryset = RecognizeVideo.objects.all()
    serializer_class = VideosListSerializer


class VideoRecognize(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = VideoRecognizeSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            video = file_serializer.data.get('video')
            obj = RecognizeVideo.objects.filter(video=video.replace('/media/', ''))
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)