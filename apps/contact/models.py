from django.db import models

from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    