from django.shortcuts import render
# Create your views here.

# Render the actual fucking page
def blog(request):
    return render(request, 'blog.html/')