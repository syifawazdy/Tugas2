from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)

