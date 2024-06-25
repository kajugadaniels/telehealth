from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
def getPatient(request, slug):
    patient = get_object_or_404(Patient, slug=slug)
    
    context = {
        'patient': patient
    }
    
    return render(request, 'patients/show.html', context)

@login_required
def editPatient(request, slug):
    pass

@login_required
def deletePatient(request, slug):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, slug=slug)
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')

    return redirect('base:getPatients')