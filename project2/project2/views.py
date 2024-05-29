from django.shortcuts import render
from django.http import HttpResponse

def home(request):      
    return HttpResponse("This is home!")
def template(request):      
    return render(request,'index.html')