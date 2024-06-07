from django.shortcuts import render,redirect
from .forms import ProfileForm

# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST)
        if profileForm.is_valid():
            profileForm.save()
            return redirect('add_profile')
    else:
        profileForm = ProfileForm()
    return render(request, 'profile.html', {'form' : profileForm})