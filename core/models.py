from django.db import models
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(default='def.png', upload_to='Posts')
    feature = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
