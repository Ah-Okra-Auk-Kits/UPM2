from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='musics/')

    class Meta:
        app_label = 'musicup'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.audio_file.delete()
        super().delete(*args, **kwargs)
