from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from base.models import *
from base.forms import *

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
@login_required
def addPatient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Patient has been added successfully.')
                return redirect('base:getPatients')
            except Exception as e:
                error_message = f'An error occurred while saving the patient: {str(e)}'
                messages.error(request, error_message)
        else:
            error_message = 'Failed to add patient. '
            for field, errors in form.errors.items():
                error_message += f"{field}: {', '.join(errors)}. "
            messages.error(request, error_message.strip())
    else:
        form = PatientForm()

    context = {
        'form': form,
    }

    return render(request, 'patients/create.html', context)

@login_required
def getPatient(request, slug):
    patient = get_object_or_404(Patient, slug=slug)
    relative = patient.relative
    
    context = {
        'patient': patient,
        'relative': relative
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