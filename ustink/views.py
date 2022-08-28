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
        return render(request, 'login.html', {'message': None})

    return HttpResponseRedirect(reverse('home'))


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'login.html', {'message': 'Login fail.'})


def logout_view(request):
    logout(request)
    return render(request, 'login.html', {'message': 'Logged out.'})


# def register_view(request):
#     if request.method == 'GET':
#         return render(request, 'register.html', {'message': None})
#     else:
#         username = request.POST['userName']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         user = authenticate(request, username=username, password=password1)
#         if user is None:
#             new_user = User.objects.create_user(username, email, password1,
#                                                 password2=password2)
#             new_user.save()
#             login(request, new_user)
#             return HttpResponseRedirect(reverse('index'))
#         else:
#             return render(request,
#                           'register.html',
#                           {'message': 'User already exists.'})

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


def edit(request):
    return render(request, 'edit.html')
