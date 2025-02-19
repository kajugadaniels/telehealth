# Generated by Django 5.0.4 on 2024-06-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrn', models.SlugField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], max_length=20, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('Rwandan', 'Rwandan'), ('other', 'Other')], default='Rwandan', max_length=50, null=True)),
                ('id_number', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('province', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('sector', models.CharField(blank=True, max_length=50, null=True)),
                ('cell', models.CharField(blank=True, max_length=50, null=True)),
                ('village', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('relative_name', models.CharField(blank=True, max_length=255, null=True)),
                ('relative_id_number', models.CharField(blank=True, max_length=50, null=True)),
                ('relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('relative_province', models.CharField(blank=True, max_length=50, null=True)),
                ('relative_district', models.CharField(blank=True, max_length=50, null=True)),
                ('relative_sector', models.CharField(blank=True, max_length=50, null=True)),
                ('relative_cell', models.CharField(blank=True, max_length=50, null=True)),
                ('relative_village', models.CharField(blank=True, max_length=50, null=True)),
                ('relative_phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name_plural': 'Patient',
            },
        ),
    ]
