from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


"""signup:nos permite automatizar la creación de los usuarios una vez se registren y poder guardar sus datos"""
def signup(request):
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  #guardamos los datos del user en la base de datos
            login(request, user)  
            return redirect('perfil')  
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})


@login_required #este decorador nos permite q solo dejemos ver la página perfil a los usarios que estén registrados
def perfil(request):
    return render(request, 'authentication/perfil.html')