from django.db import models
from django.contrib.auth.forms import User
from django.core.validators import MinValueValidator, MaxValueValidator
import time
import datetime

class Records(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    datetime = models.DateTimeField(default = datetime.datetime.now())
    recording = models.BooleanField(default = False)
    continued = models.BooleanField(default = False)
    relative_path = models.CharField(max_length = 30, null = True)

class Settings(models.Model):
    recording = models.BooleanField()
    path = models.CharField(max_length=200, null = True)
    fps = models.PositiveIntegerField(validators=[MinValueValidator(5),
                                         MaxValueValidator(30)])

