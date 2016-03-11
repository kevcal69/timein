from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class TimeInView(TemplateView):
    template_name = "timein/login.html"
