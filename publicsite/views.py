
from django.shortcuts import render

# Create your views here.

def home(request):
    title = "Welcome to Yotta Robotics"
    page = {"title":title}
    return render(request, 'publicsite/index.html', {'name': home,'page':page})