from django.shortcuts import render

# Create your views here.

def home(request):
    title = "Welcome to Yotta Robotics"
    page = {"title":title}
    return render(request, 'publicsite/index.html', {'name': home,'page':page})

def about(request):
    return render(request, 'publicsite/commom/about.html', {'about': about})

def services(request):
    return render(request, 'publicsite/commom/services.html', {'services': services})

def products(request):
    return render(request, 'publicsite/products.html', {'products': products})

def blog(request):
    return render(request, 'blog/blog-home.html', {'blog': blog})

def contact(request):
    return render(request, 'publicsite/commom/contact.html', {'contact': contact})

def join(request):
    return render(request, 'publicsite/user/join.html', {'join': join})