from django.db import models
from django.conf import settings
# Create your models here.

def update_status_image(instance, filename):
    return "status/{user}/{filename}".format(filename=filename, user=instance.user)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to=update_status_image)
    updates = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or "this status has no content"

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
