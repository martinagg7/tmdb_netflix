from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, perfil


"""Usamos directamente las vistas Login y Logout de django que crean un formulario para que cada usuario indique su nombre y contraseña"""

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('perfil/', perfil, name='perfil'),
]