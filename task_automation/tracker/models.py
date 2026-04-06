from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()
    frequency = models.CharField(max_length=20)

    def __str__(self):
        return self.name