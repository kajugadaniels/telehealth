# Generated by Django 5.0.4 on 2024-06-25 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_patient_created_at_patient_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name_plural': 'Patients'},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
    ]
