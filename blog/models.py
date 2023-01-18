from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'publish'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='/images/', blank=True, null=True)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='post')
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
