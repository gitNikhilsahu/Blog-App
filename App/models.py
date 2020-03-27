from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone



STATUS=(
    (0, "Draft"),
    (1, "Publish")
)

class Article(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, blank=True, unique=True)
    # tags
    featured = models.BooleanField(default=False)
    status=models.IntegerField(choices=STATUS, default=0)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_app')
    updated_on=models.DateTimeField(auto_now=True)
    created_on=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(blank=True, null=True)
    article_image=models.FileField(upload_to='Article/%Y/%m/%d/', blank=True, null=True)
    description=models.TextField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        self.slug=self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('articleretrive', kwargs={"id":self.id})

    class Meta:
        ordering=['-created_on']
        verbose_name_plural = "Articles"
