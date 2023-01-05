from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'vanaja'}
    return render(request,'first.html',d)