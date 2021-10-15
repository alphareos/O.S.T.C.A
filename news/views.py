from django.shortcuts import render
from .models import Post
# importing paginator
from django.core.paginator import Paginator


# Create your views here.
def post(request):
    posts = Post.objects.all().order_by('pub_date')
    # setting up paginator
    p = Paginator(posts, 3)
    p2 = Paginator(posts, 4)
    page = request.GET.get('page')
    postPaginator = p.get_page(page)
    recentPostPaginator = p2.get_page(page)
    return render(request, 'blog.html', {'postPaginator': postPaginator, 'recentPostPaginator': recentPostPaginator})


def Post_detail(request, slug):
    posts = Post.objects.get(slug=slug)
    posted = Post.objects.all().order_by('pub_date')
    p2 = Paginator(posted, 5)
    page = request.GET.get('page')
    recentPostPaginator = p2.get_page(page)

    return render(request, 'blog-single.html', {'posts': posts, 'post': posted, 'recentPostPaginator': recentPostPaginator})

def search(request):
    return render(request, 'search.html')