from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg
from .models import Review
from .forms import ReviewForm


def review_list(request):
    reviews = Review.objects.filter(is_approved=True)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    paginator = Paginator(reviews, 6)
    page_obj = paginator.get_page(request.GET.get('page'))

    form = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                messages.success(request, 'Thank you! Your review has been submitted and is awaiting approval.')
                return redirect('reviews:list')
        else:
            form = ReviewForm()

    return render(request, 'reviews/review_list.html', {
        'page_obj': page_obj,
        'avg_rating': round(avg_rating, 1),
        'total_reviews': reviews.count(),
        'form': form,
    })
