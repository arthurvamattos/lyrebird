from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [    
    # path('perfil/', views.exibir_perfil, name='perfil'),
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='entrar'),
    path('sair/', auth_views.LogoutView.as_view(template_name='index.html'), name="sair"),
    path('registrar/', views.registrar, name='registrar'),
    # path('recuperar/', views.passwordReset, name='passwordReset'),
    # path('confirmar/<str:key>/', views.passwordResetConfirm, name='passwordResetConfirm'),
]
