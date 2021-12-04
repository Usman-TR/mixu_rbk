from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from neural.tools import create_audio, transcribe 


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
            video = file_serializer.data.get('video')[1:]
            obj = RecognizeVideo.objects.filter(video=video.replace('/media/', ''))
            audio = create_audio(video)
            text = transcribe(audio)
            obj.transcript = text.get('transcript')
            obj.transcript_with_timestamps = text.get('text_with_timestamps')
            return Response({'text': text},  status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)