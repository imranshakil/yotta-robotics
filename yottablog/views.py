from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>This is a blog page</h1>")

def blog_main(request):
    return render(request, 'blog/main.html', {'blog-main': blog_main})

def blog_header(request):
    return render(request, 'blog/common/blog_header.html', {'blog_header': blog_header})

def blog_menu(request):
    return render(request, 'blog/post/blog_menu.html', {'blog_menu': blog_menu})

def highlight(request):
    return render(request, 'blog/post/highlight.html', {'highlight': highlight})

def public_news_feed(request):
    return render(request, 'blog/post/public_news_feed.html', {'public_news_feed': public_news_feed})

