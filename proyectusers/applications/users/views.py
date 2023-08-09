# Python
from typing import Any, Dict
from .functions import code_generator
# Djengo
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,
    CreateView,
    UpdateView,
)
from django.views.generic.edit import (
    FormView,
)
# Models
from .models import User
# Forms
from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    VerificationForm,
)


# Register User 
class UserRegisterView(FormView):    
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url =  reverse_lazy ('home_app:user-panel')
    
    def form_valid(self, form):
        # Generamos el Codigo
        codigo = code_generator()

        user = User.objects.create_user(
            form.cleaned_data['username'], 
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            name = form.cleaned_data['name'],
            last_name = form.cleaned_data['last_name'],
            gender = form.cleaned_data['gender'],
            cod_register= codigo
        )
        
        # Enviar el codigo al Email
        subject = "Email Conformation"
        message = 'Verification Code:'+ ' ' + codigo
        sender_email = 'agustin.r.estudio@gmail.com'
        send_mail(subject, message, sender_email, [form.cleaned_data['email'],] )
        
        # Redigir a pantalla de validacion
        
        return HttpResponseRedirect(
            reverse(
                'users_app:user-verification',
                kwargs = {'pk':user.id },
            )
        )


# Login User
class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy ('home_app:user-panel')
    
    def form_valid(self, form):
        user = authenticate(
            username =  form.cleaned_data['username'],
            password = form.cleaned_data['password1'],
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


# Logout User
class LogoutUser(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login',
            )
        )


# Update User
class UpdateUSer(LoginRequiredMixin, UpdateView):
    model = User
    fields = [
        'username',
        'email',
        'name',
        'last_name',
        'gender',
    ]
    template_name = "users/update.html"
    login_url = reverse_lazy('users_app:user-login')
    success_url = reverse_lazy ('home_app:user-panel')
    

# Update Password USer
class UpdatePasswordUser(LoginRequiredMixin, FormView):
    template_name = 'users/updatepassword.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy ('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')
    
    def form_valid(self, form):
        # Usuario logeado
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            
        logout(self.request)

        return super(UpdatePasswordUser, self).form_valid(form)


# Code Verification
class CodeVerificationsView(FormView):
    
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy ('users_app:user-login')
    
    def get_form_kwargs(self) :
        kwargs = super(CodeVerificationsView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk']
        })
        return kwargs
    
    def form_valid(self, form):
        
        User.objects.filter(
            id = self.kwargs['pk']
        ).update(
            is_active = True
        )
        return super(CodeVerificationsView, self).form_valid(form)
