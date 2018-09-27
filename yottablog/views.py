from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>This is a blog page</h1>")

def blog_main(request):
    return render(request, 'blog/main.html', {'blog-main': blog_main})