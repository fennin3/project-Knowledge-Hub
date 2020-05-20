from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AccountTypeForm
from django.contrib import messages


# Create your views here.

def signin(request):
    return render(request, 'users/login.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can now log in ')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/signup.html', {'form': form})


def edit_profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been Updated!')
			return redirect('home')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)	
 
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/edit_profile.html', context)



def account_type(request):
	if request.method == 'POST':
		form = AccountTypeForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			messages.success(request, f'Welcome New User!')
			return redirect('home')
	else:
		form = AccountTypeForm(instance=request.user.profile)
	return render(request, 'users/account_type.html', {'form':form})


