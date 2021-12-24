from django.db import models

class String(models.Model):
    name     = models.CharField('String value name', max_length=255)
    contents = models.CharField('String value contents', max_length=16384)

    def __str__(self):
        return self.contents