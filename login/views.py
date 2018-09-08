from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader



def index(request):
    # template_name = 'index.html'
    # return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('login/index.html')
    context = {
        'latest_question_list': '',
    }
    return HttpResponse(template.render(context, request))