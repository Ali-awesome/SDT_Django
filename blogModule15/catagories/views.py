from django.shortcuts import render,redirect
from .forms import CategoryForm

# Create your views here.
def add_catagory(request):
    if request.method == 'POST':
        categoryFrom = CategoryForm(request.POST)
        if categoryFrom.is_valid():
            categoryFrom.save()
            return redirect('add_catagory')
    else:
        categoryFrom = CategoryForm()
    return render(request, 'catagory.html',{'form' : categoryFrom})
