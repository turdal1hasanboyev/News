from django.db import models

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
