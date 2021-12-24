from django.shortcuts import render
from .models import String
# Create your views here.

# Render the actual fucking page
def home(request):
    context = {}
    for string in String.objects.all():
        context[string.name] = string.contents
    return render(request, 'home.html/', {"string":context})