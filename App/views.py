from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm #form 

from django.contrib import messages #user register then message pass to login  page account created

from .forms import CreateUserForm, NewForm


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *



def AccountsHome(request):
    context = {}
    return render(request, 'Accounts/AccountsHome.html', context)

def registerPage(request):
	# form = UserCreationForm() #form
	form = CreateUserForm() #from
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')

	context ={'form': form}
	return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('accountshome')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context ={}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')




def article_home(request):
    Articles = Article.objects.all()
    context = {'Articles': Articles}
    return render(request, 'Article/ArticleHome.html', context)
 
def article_list(request):
    Articles = Article.objects.all()
    context = {'Articles': Articles}
    return render(request, 'Article/ArticleList.html', context)

def article_create(request):
    form = NewForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/article')
    context = {'form':form}
    return render(request, 'Article/ArticleCreate.html', context)

def article_retrive(request, id=None):
    instance = get_object_or_404(Article, id=id)
    context={'instance':instance}
    return render(request, "Article/ArticleRetrive.html", context)

def article_update(request, id=None):
    instance = get_object_or_404(Article, id=id)
    form = NewForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'instance':instance, 'form':form}
    return render(request, 'Article/ArticleUpdate.html', context)

def article_delete(request, id=None):
    instance = get_object_or_404(Article, id=id)    
    instance.delete()
    return render(request, 'Article/ArticleDelete.html')