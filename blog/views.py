from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category


def post_list(request):
    posts = Post.objects.filter(status='published')
    category_slug = request.GET.get('category')
    query = request.GET.get('q')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    if query:
        posts = posts.filter(title__icontains=query)
    paginator = Paginator(posts, 6)
    page_obj = paginator.get_page(request.GET.get('page'))
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'categories': categories, 'query': query or ''})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    recent_posts = Post.objects.filter(status='published').exclude(id=post.id)[:4]
    return render(request, 'blog/post_detail.html', {'post': post, 'recent_posts': recent_posts})
