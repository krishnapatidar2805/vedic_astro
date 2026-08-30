from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Service


def service_list(request):
    services = Service.objects.filter(is_active=True)
    paginator = Paginator(services, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'services/service_list.html', {'page_obj': page_obj, 'services': page_obj})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related = Service.objects.filter(is_active=True).exclude(id=service.id)[:3]
    return render(request, 'services/service_detail.html', {'service': service, 'related': related})
