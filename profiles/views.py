from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from .models import Profile


@login_required()
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profiles/me.html', {'profile':profile})




def user_profile(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Profile.DoesNotExist:
        return Http404

    return render(request, 'profiles/user.html', {'profile': profile})