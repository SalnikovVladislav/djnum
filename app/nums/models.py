import uuid

from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255, default=str(uuid.uuid4()))
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=255, default="-1")
    nn_answer = models.CharField(max_length=255, default="", null=True)