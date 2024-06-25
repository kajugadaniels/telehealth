from django.urls import path
from django.conf import settings
from base.views import *
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),

    path('patients', getPatients, name='getPatients'),
    path('patient/add', addPatient, name='addPatient'),
    path('patient/<slug>', getPatient, name='getPatient'),
    path('patient/<slug>/edit', editPatient, name='editPatient'),
    path('patient/<slug>/delete', deletePatient, name='deletePatient'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)