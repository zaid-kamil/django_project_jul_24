from django.db import models

class Task(models.Model):
    name = models.CharField(max_length = 150)
    completed = models.BooleanField(default=False)    

# 1. python manage.py makemigrations
# 2. python manage.py migrate