from django.views.generic import TemplateView

class IndexPageView(TemplateView):
    template_name = "index.html"

"""from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Mensaje, Hola mundo.")

"""