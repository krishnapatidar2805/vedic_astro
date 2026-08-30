from django.shortcuts import render
from django.core.paginator import Paginator
from .models import GalleryImage, GalleryCategory


def gallery_view(request):
    images = GalleryImage.objects.filter(is_active=True)
    category_id = request.GET.get('category')
    if category_id:
        images = images.filter(category_id=category_id)
    paginator = Paginator(images, 12)
    page_obj = paginator.get_page(request.GET.get('page'))
    categories = GalleryCategory.objects.all()
    return render(request, 'gallery/gallery.html', {'page_obj': page_obj, 'categories': categories})
