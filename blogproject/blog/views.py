from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    blogs = models.BlogModel.objects.filter(is_active=True)
    categories = models.Category.objects.all()
    last4blogs = models.BlogModel.objects.filter(is_active=True).order_by('-id')[:4]
    last4blogsReserveds = reversed(last4blogs)
    context = {
        "blogs": blogs,
        "last4blogsReserveds": last4blogsReserveds,
        "categories": categories
    }
    return render(request, "index.html", context)

def blogs(request):
    blogs = models.BlogModel.objects.filter(is_active=True)
    categories = models.Category.objects.all()
    context = {
        "blogs": blogs,
        "categories": categories
    }
    return render(request, "blogs.html", context)

def blog_detail(request, slug):
    blogs = models.BlogModel.objects.get(slug=slug)
    categories = models.Category.objects.all()
    icerik = {"blog": blogs, "categories": categories}

    return render(request, "blog_detail.html", icerik)

def blog_by_category(request, slug):
    blogs = models.Category.objects.get(slug=slug).blogmodel_set.filter(is_active=True)
    categories = models.Category.objects.all()
    context = {
        "blogs": blogs,
        "categories": categories,
        "selected_category": slug
    }
    return render(request, "blogs.html", context=context)
