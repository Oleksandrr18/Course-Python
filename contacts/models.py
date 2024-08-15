from django.db import models


# Create your models here.
class Contacts(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contacts'
