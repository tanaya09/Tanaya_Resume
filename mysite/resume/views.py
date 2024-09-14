from django.shortcuts import render
from django.http import HttpResponse

#def home(request):
    #return HttpResponse("Hello, this is my CV page!")
def home(request):
    return render(request, 'resume/cv.html')

# Create your views here.
