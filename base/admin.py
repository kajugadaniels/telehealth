from django.contrib import admin
from base.models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'id_number', 'phone_number', 'marital_status', 'nationality')

admin.site.register(Patient, PatientAdmin)