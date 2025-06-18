from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect('home') # We'll name our homepage URL 'home' later
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})