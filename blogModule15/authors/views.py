from django.shortcuts import render, redirect
from .forms import AuthorForm

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        authorForm = AuthorForm(request.POST)
        if authorForm.is_valid():
            authorForm.save()
            return redirect('add_author')
    else:
        authorForm = AuthorForm()
    return render(request, 'author.html', {'form' : authorForm})
