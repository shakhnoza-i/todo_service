from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    complete_time = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self): 
        return self.name
