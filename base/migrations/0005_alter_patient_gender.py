# Generated by Django 5.0.4 on 2024-06-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_patient_slug_alter_patient_mrn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
    ]
