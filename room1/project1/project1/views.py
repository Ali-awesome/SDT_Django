from django.http import HttpResponse
def home(request):
    return HttpResponse("This is our home page!")
def contact(request):
    return HttpResponse("This is our contact page!")