from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Sub_Email(BaseModel):
    sub_email = models.EmailField(unique=True, max_length=150)

    def __str__(self):
        return self.sub_email
