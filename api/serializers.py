from rest_framework import serializers
from recognize_videos.models import RecognizeVideo
#from neural.tools import create_audio
class VideosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognizeVideo
        fields = ('id', 'created_date', 'transcript', 'transcript_with_timestamps')


class VideoRecognizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognizeVideo
        fields = ('video', )

