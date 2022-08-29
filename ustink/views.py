from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .models import message, customer
from .forms import homeForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from frontend.forms import CreateUserForm


def home(request):
    return render(request, 'home.html')


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'message': ' با موفقیت وارید شدید '})

    return HttpResponseRedirect(reverse('home'))


def LoginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'login.html', {'message': ' لطفا دوباره متحان کنید '})


# def logout_view(request):
#     logout(request)
#     return render(request, 'login.html', {'message': 'Logged out.'})


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = CreateUserForm
    redirect_authenticated_user = _name = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


def contactus(request):
    return render(request, 'contactus.html')


@login_required(redirect_field_name='index')
def edit(request):
    return render(request, 'edit.html')


@login_required(redirect_field_name='index')
def completeProfile(request):
    return render(request, 'completeProfile.html')
