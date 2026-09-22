import urllib.parse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from services.models import Service


def get_appointment_whatsapp_url(appointment):
    phone_number = settings.BUSINESS_WHATSAPP
    service_name = appointment.service.title if appointment.service else "Vedic Consultation"
    dob_str = appointment.date_of_birth.strftime('%d/%m/%Y') if appointment.date_of_birth else "उपलब्ध नहीं"
    tob_str = appointment.time_of_birth.strftime('%I:%M %p') if appointment.time_of_birth else "उपलब्ध नहीं"
    pref_date_str = appointment.preferred_date.strftime('%d/%m/%Y') if appointment.preferred_date else "N/A"
    pref_time_str = appointment.preferred_time.strftime('%I:%M %p') if appointment.preferred_time else "N/A"
    mode_display = appointment.get_consultation_mode_display()
    
    text = (
        f"🙏 जय श्री राम, पंडित जी!\n"
        f"मैंने आपकी वेबसाइट ({settings.SITE_NAME}) से परामर्श/पूजा बुक की है:\n\n"
        f"📋 बुकिंग आईडी: #APP-{appointment.id:04d}\n"
        f"👤 यजमान का नाम: {appointment.full_name}\n"
        f"📞 मोबाइल नंबर: {appointment.phone}\n"
        f"🔮 सेवा: {service_name}\n"
        f"📅 पसंदीदा तारीख: {pref_date_str}\n"
        f"⏰ पसंदीदा समय: {pref_time_str}\n"
        f"📱 माध्यम: {mode_display}\n\n"
        f"📜 जन्म कुंडली विवरण:\n"
        f"🎂 जन्म तिथि: {dob_str}\n"
        f"🕒 जन्म समय: {tob_str}\n"
        f"📍 जन्म स्थान: {appointment.place_of_birth or 'उपलब्ध नहीं'}\n\n"
        f"💬 समस्या/प्रश्न:\n{appointment.message or 'परामर्श हेतु संपर्क'}\n\n"
        f"कृपया मेरा समय स्लॉट कन्फर्म करने की कृपा करें। सादर प्रणाम!"
    )
    encoded = urllib.parse.quote(text)
    return f"https://wa.me/{phone_number}?text={encoded}"


@login_required
def book_appointment(request):
    preselected_service = request.GET.get('service')
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'आपकी बुकिंग दर्ज हो गई है! पंडित जी को WhatsApp पर भेजकर समय कन्फर्म करें।')
            return redirect('appointments:success', pk=appointment.pk)
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


@login_required
def booking_success(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    whatsapp_url = get_appointment_whatsapp_url(appointment)
    return render(request, 'appointments/booking_success.html', {
        'appointment': appointment,
        'whatsapp_url': whatsapp_url,
    })
