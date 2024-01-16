from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

# i will continue working on this tomorrow insha Allah