from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost 


def blog_page(request):
    blog_post = BlogPost.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(blog_post, 6)

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

def blog_detail(request, id):
    blog_detail = get_object_or_404(BlogPost, id=id)
    paragraphs = blog_detail.content.split('\n')
    paragraphs_conf = []
    
    for p in paragraphs:
        if not p.strip():
            continue

        words = p.split()
        word_one = words[0] if words else ""
        
        if (word_one == "!subtitle!" or word_one == "!image!"):
            words.pop(0)
            p = ' '.join(words)

        paragraphs_conf.append({
            'word_one' : word_one,
            'text' : p
        })
    
    print("paragrafos: ", [ p['word_one'] for p in paragraphs_conf])

    context = {
        'blog': blog_detail,
        'paragraphs': paragraphs_conf
    }

    return render(request, 'content-blog.html', context)
