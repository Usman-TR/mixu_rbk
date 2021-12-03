from django.db import models

class RecognizeVideo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='created date')
    transcript = models.TextField(blank=True, null=True, verbose_name='transcript')
    transcript_with_timestamps = models.TextField(blank=True, null=True, verbose_name='transcript with timestamps')
    video = models.FileField(upload_to='videos', verbose_name='video')
    
    def __str__(self) -> str:
        return self.title