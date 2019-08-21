from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.conf import settings
# from .forms import RegisterForm, EditarPerfilForm, PasswordResetForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from .utils import generate_hash_key

User = get_user_model()


def registrar(request):
    context = {}
    form = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()

    context['form'] = form
    return render(request, 'registrar.html', context)

'''
def passwordReset(request):
    context={}
    form = PasswordResetForm(request.POST or None)
    if (form.is_valid()):
        form.save()
        context['success'] = True        
    context['form'] = form
    return render(request, 'reset_password.html', context)



def passwordResetConfirm(request, key):
    context={}
    usuario = PasswordReset.objects.get(key=key).user 
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=usuario, data=request.POST or None)
    if (form.is_valid()):
        form.save()
        context['success'] = True    
    else:
        for e in form.error_messages:
            print(e)
    context['form'] = form
    return render(request, 'password_reset_confirm.html', context)
'''

@login_required
def exibir_perfil(request): 
    context = {}
    context['perfil'] = request.user
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        formPass = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.profile_pic = request.FILES['profile_pic']
            form.save()
            form = EditarPerfilForm(instance=request.user)
        else:
            print(form.errors)
        if formPass.is_valid():
            formPass.save()
        else:
            print(formPass.errors)
    else:
        form = EditarPerfilForm(instance=request.user)
        formPass = PasswordChangeForm(user=request.user)
    context['form'] = form
    context['formPass'] = formPass
    return render(request, 'perfil.html', context)