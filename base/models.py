import os
import random
import string
from django.db import models
from datetime import date
from django.utils import timezone
from django.utils.text import slugify
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

def patient_image_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return f'patients/{slugify(instance.name)}_{instance.dob}_{instance.gender}_{instance.id_number}{file_extension}'

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
    ]

    NATIONALITY_CHOICES = [
        ('Rwandan', 'Rwandan'),
        ('Other', 'Other'),
    ]

    RELATIONSHIP_CHOICES = [
        ('Husband', 'Husband'),
        ('Wife', 'Wife'),
        ('Sibling', 'Sibling'),
        ('Friend', 'Friend'),
        ('Other Family Member', 'Other Family Member'),
    ]

    mrn = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    image = ProcessedImageField(
        upload_to=patient_image_path,
        processors=[ResizeToFill(720, 720)],
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, default='Rwandan', null=True, blank=True)
    id_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    sector = models.CharField(max_length=50, null=True, blank=True)
    cell = models.CharField(max_length=50, null=True, blank=True)
    village = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES, null=True, blank=True)
    relative = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='relatives')
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def age(self):
        if self.dob:
            today = date.today()
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return None

    def generate_mrn(self):
        while True:
            mrn = 'MRN-' + ''.join(random.choices(string.digits, k=10))
            if not Patient.objects.filter(mrn=mrn).exists():
                return mrn

    def save(self, *args, **kwargs):
        if not self.mrn:
            self.mrn = self.generate_mrn()
        if not self.slug and self.name and self.dob and self.gender and self.id_number:
            self.slug = slugify(f'{self.name}-{self.dob}-{self.gender}-{self.id_number}')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Patients"

    def __str__(self):
        return self.name if self.name else "Patient"
