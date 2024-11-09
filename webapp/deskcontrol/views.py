from django.shortcuts import render

# Create your views here.
# myapp/views.py
def index(request):
    return render(request, 'homepage/index.html')
