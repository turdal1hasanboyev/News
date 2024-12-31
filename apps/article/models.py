from django.db import models

from django.utils.text import slugify
from django.urls import reverse

from apps.common.models import BaseModel
from apps.category.models import Category, Tag
from apps.account.models import CustomUser


class Article(BaseModel):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='article_images/')
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='articles_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles_category')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles_tags')
    views = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('article-detail', kwargs={'slug': self.slug})
