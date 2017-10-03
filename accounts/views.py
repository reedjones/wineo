__author__ = 'reed'

from django.shortcuts import render
from . import forms
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout, authenticate
from profiles.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                name=form.cleaned_data['name'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )

            profile = Profile(
                user=user,
                nick=data['nick'],
                description=data.get("description", None))
            profile.save()

            authenticated = authenticate(email=data['email'],
                                         password=data['password1'])

            if authenticated is not None and not request.user.is_authenticated():
                login(request, authenticated)
                return HttpResponseRedirect(reverse('add_photo'))

            #wait should this be here? if reach here there is an error
            return HttpResponse("bad")

        else:
            return render(request, 'accounts/signup.html', {'form': form})

    else:
        form = forms.RegistrationForm()

    return render(request, 'accounts/signup.html' ,{
        'form': form
    })


@login_required()
def add_photo(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.photo = request.FILES['image']
            profile.save()

            return HttpResponseRedirect("/profiles/my_profile/")
        else:
            return render(request, 'accounts/add_photo.html', {'form': form})
    else:
        form = forms.ImageForm()
    return render(request, 'accounts/add_photo.html', {'form': form})



def login_(request):
    pass



@login_required()
def logout_(request):
    pass

