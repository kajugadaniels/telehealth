# Generated by Django 5.0.4 on 2024-06-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_patient_relative_cell_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='relationship',
            field=models.CharField(blank=True, choices=[('Husband', 'Husband'), ('Wife', 'Wife'), ('Sibling', 'Sibling'), ('Friend', 'Friend'), ('Other Family Member', 'Other Family Member')], max_length=50, null=True),
        ),
    ]
