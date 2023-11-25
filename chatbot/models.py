from django.db import models

class Past(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.question
