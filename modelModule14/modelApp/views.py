from django.shortcuts import render,redirect
from . import models
# Create your views here.

def Home(request):
    person = models.Person.objects.all()
    return render(request, 'modelApp/home.html', {'data' : person})

def Delete(request, userId):
    id = models.Person.objects.get(pk = userId).delete()
    print(id)
    return redirect("home")