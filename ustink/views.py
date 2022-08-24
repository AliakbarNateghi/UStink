from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import message
from .forms import homeForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def getName(request):
    if request.method == 'POST':
        form = homeForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']

        if form.is_valid():
            return HttpResponseRedirect('thanks.html')

    else:
        form = homeForm()

    return render(request, 'home.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')


# if form.is_valid():
#     subject = form.cleaned_data['subject']
#     message = form.cleaned_data['message']
#     sender = form.cleaned_data['sender']
#     cc_myself = form.cleaned_data['cc_myself']
#
#     recipients = ['info@example.com']
#     if cc_myself:
#         recipients.append(sender)
#
#     send_mail(subject, message, sender, recipients)
#     return HttpResponseRedirect('/thanks/')
