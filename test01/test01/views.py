#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('Homepage')
    return render(request, 'home.html')


def about(request):
    #return HttpResponse('About')
    return render(request, 'about.html')

