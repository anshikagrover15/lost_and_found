from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'myapp/index.html')

def found(request):
    items = Found.objects.all()
    if request.method == 'GET':
        return render(request, 'myapp/found.html', {'form':FoundForm(), 'items':items})
    else: 
        try:
            form = FoundForm(request.POST, request.FILES)
            form.save()
            return redirect('found')
        except ValueError:
            return render(request, 'myapp/found.html', {'form':form, 'items': items, 'error': 'Bad Info!'})
       
def lost(request):
    items = Lost.objects.all()
    if request.method == 'GET':
        return render(request, 'myapp/lost.html', {'form': LostForm(), 'items':items})
    else:
        try:
            form = LostForm(request.POST, request.FILES)
            form.save()
            return redirect('lost')
        except ValueError:
            return render(request, 'myapp/lost.html', {'form': LostForm(), 'error': 'Bad info!', 'items':items})




