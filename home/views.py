from django.shortcuts import render, redirect
from .models import Blog
from .models import BlogCategory
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from home.forms import NewsCreateForm, NewsEditForm, CategoryCreateForm
from django.contrib.auth.decorators import login_required

import random
import os

items = list(Blog.objects.all())

# Create your views here.
def home(req):

    popBlog = []
    if len(items) > 2:
        popBlog = random.sample(items, 2)

    blog = Blog.objects.all().order_by('-id')
    category = BlogCategory.objects.all()

    paginator = Paginator(blog, 30)
    page = req.GET.get('page', 1) # websitenin url kısmına girilen değeri uygula ve default 1 olsun
    blog = paginator.page(page)

    context = {
        "blogs" : blog, 
        "popBlogs": popBlog,
        "categorys" : category,
    }

    return render(req, "home/blogList.html", context)


def categoryList(req, catSlugName):

    blog = Blog.objects.filter(categorys__slug = catSlugName).order_by('-id')
    categoryName = catSlugName.replace("-", " ").title()

    popBlog = []
    if len(items) > 2:
        popBlog = random.sample(items, 2)

    category = BlogCategory.objects.all()

    paginator = Paginator(blog, 30)
    page = req.GET.get('page', 1) 
    blog = paginator.page(page)


    context = {
        "categoryName": categoryName,
        "popBlogs": popBlog,
        "blogs" : blog,  
        "categorys" : category,
    }

    return render(req, "home/blogCatList.html", context)


def blogText(req, BlogSlugName):

    items = list(Blog.objects.all())

    popBlog = []
    if len(items) > 2:
        popBlog = random.sample(items, 2)

    blog = get_object_or_404(Blog, slug=BlogSlugName)
    category = BlogCategory.objects.all()

    context = {
        "blogs" : blog,     
        "popBlogs": popBlog,   
        "categorys" : category,
    }
    return render(req, "home/blogText.html", context)


# ADMİN ----------------------------------------------------------------------


@login_required()
def news_list(req):
    blog = Blog.objects.all().order_by('-id')
    category = BlogCategory.objects.all()

    paginator = Paginator(blog, 30)
    page = req.GET.get('page', 1) 
    blog = paginator.page(page)


    context = {
        "blogs" : blog,
        "categorys" : category,
    }
    return render(req, "home/AlistBlog.html", context)

@login_required()
def news_edit(req, newsId):
    blog = get_object_or_404(Blog, pk=newsId)
    category = BlogCategory.objects.all()

    if req.method == "POST":
        form = NewsEditForm(req.POST , instance=blog)
        form.save()
        return redirect("news_list")

    form = NewsEditForm(instance=blog)

    context = {
        "form": form,
        "categorys" : category,
    }
    return render(req, "home/AeditBlog.html", context)

@login_required()
def news_delete(req, newsId):
    blog = get_object_or_404(Blog, pk=newsId)
    category = BlogCategory.objects.all()

    if req.method == "POST":
        if len(blog.image) > 0:
            os.remove(blog.image.path)
        blog.delete()
        return redirect("news_list")

    context = {
        "blogs": blog,
        "categorys" : category,
    }
    return render(req, "home/AdeleteBlog.html", context)

@login_required()
def create_news(req):
    category = BlogCategory.objects.all()

    if req.method == "POST":
        form = NewsCreateForm(req.POST, req.FILES)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NewsCreateForm()

    context = {
        "form": form,
        "categorys" : category,
    }
    return render(req, "home/AcreateBlog.html", context)

@login_required()
def create_category(req):
    category = BlogCategory.objects.all()

    if req.method == "POST":
        form = CategoryCreateForm(req.POST, req.FILES)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoryCreateForm()

    context = {
        "form": form,
        "categorys" : category,
    }
    return render(req, "home/AcreateCategory.html", context)