from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página principal
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})