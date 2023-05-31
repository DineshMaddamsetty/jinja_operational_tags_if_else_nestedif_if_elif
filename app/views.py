from django.shortcuts import render

def dinesh(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'conditional.html',d)
# Create your views here.

def looping(request):
    d={'name':'Dinesh'}
    return render(request,'loop.html',d)

def nestedif(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'nested.html',d)

