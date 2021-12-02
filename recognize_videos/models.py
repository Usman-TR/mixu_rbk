from django.db import models

class RecognizeVideo(models.Model):
    title = models.CharField(max_length=500, verbose_name='title')
    topic = models.CharField(max_length=1000, verbose_name='topic')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='created date')
    transcript = models.TextField(blank=True, null=True, verbose_name='transcript')
    transcript_by_keywords = models.TextField(blank=True, null=True, verbose_name='transcript by keywords')
    transcript_with_timestamps = models.TextField(blank=True, null=True, verbose_name='transcript with timestamps')
    
    def __str__(self) -> str:
        return self.title