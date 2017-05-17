from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def after_login(request):
    return render(request, 'personal/login.html', locals())


def home(request):
    return render(request, 'personal/home.html', locals())


def user_login(request):
    postdata = request.POST.copy()
    username = postdata.get("username", "")
    password = postdata.get("password", "")
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        url = urlresolvers.reverse('personal:after_login')
        return HttpResponseRedirect(url)
    else:
        error = "check your username and password!"
        return render(request, 'personal/home.html', locals())


def logout(request):
    logout(request)
    url = urlresolvers.reverse('personal:after_login')
    return HttpResponseRedirect(url)
