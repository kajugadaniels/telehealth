from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from base.models import *

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def getPatients(request):
    patients = Patient.objects.all().order_by('-created_at')

    context = {
        'patients': patients
    }

    return render(request, 'patients/index.html', context)

@login_required
def addPatient(request):
    pass

@login_required
def getPatient(request, mrn):
    pass

@login_required
def editPatient(request, mrn):
    pass

@login_required
def deletePatient(request, mrn):
    pass