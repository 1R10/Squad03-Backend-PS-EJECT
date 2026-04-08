from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost 


def blog_page(request):
    blog_post = BlogPost.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(blog_post, 5)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        'blog_post': result
    }

    return render(request, 'blog.html', context)
