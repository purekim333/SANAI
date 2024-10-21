from django.shortcuts import render, redirect
from .models import Popular


# Create your views here.
def index(request):
    populars = Popular.objects.all()
    context = {
        'populars' : populars
    }
    return render(request, 'sanais/index.html', context)

def introduce(request):
    return render(request, 'sanais/introduce.html')


def profile(request):
    return render(request, 'sanais/profile.html')