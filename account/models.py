import os
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

def user_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'users/{slugify(instance.name)}_{instance.role}_{instance.gender}_{instance.id_number}{file_extension}'

class User(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.SlugField(unique=True, blank=True)
    email = models.CharField(max_length=30, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    id_number = models.CharField(unique=True, max_length=20, null=True, blank=True)
    image = ProcessedImageField(
        upload_to=user_image_path,
        processors=[ResizeToFill(720, 720)],
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']
    
    class Meta:
        verbose_name_plural = "Users"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name