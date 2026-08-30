from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from services.models import Service


@login_required
def book_appointment(request):
    preselected_service = request.GET.get('service')
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Your appointment request has been submitted! We will contact you shortly to confirm.')
            return redirect('appointments:history')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        initial = {}
        if preselected_service:
            service_obj = Service.objects.filter(slug=preselected_service).first()
            if service_obj:
                initial['service'] = service_obj
        initial['full_name'] = request.user.get_full_name() or request.user.username
        initial['phone'] = request.user.profile.phone
        initial['email'] = request.user.email
        form = AppointmentForm(initial=initial)
    return render(request, 'appointments/book_appointment.html', {'form': form})


@login_required
def appointment_history(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/appointment_history.html', {'appointments': appointments})


@login_required
def appointment_cancel(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if appointment.status in ['pending', 'confirmed']:
        appointment.status = 'cancelled'
        appointment.save()
        messages.success(request, 'Appointment cancelled successfully.')
    return redirect('appointments:history')
