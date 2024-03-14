from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms

from guitar_house.accounts.forms import GuitarUserCreationForm


# Create your views here.
class Signupuserview(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = GuitarUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.user)

        return result


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


def sign_out(request):
    logout(request)
    return redirect('index')