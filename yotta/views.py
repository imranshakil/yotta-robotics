from django.shortcuts import render

# Create your views here.

def log_reg_views(request):
    return render(request, 'yotta/login.html', {'log_reg_view': log_reg_views})