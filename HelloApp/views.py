from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello World. This is the index")
    return render(request, 'HelloApp/index.html')
