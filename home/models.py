from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=255)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
    class Meta:
        app_label = 'home'
