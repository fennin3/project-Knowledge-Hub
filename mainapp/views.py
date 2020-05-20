from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from users.forms import AccountTypeForm
from django.contrib import messages


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.account_type != 'Select':
            return render(request, 'mainapp/index.html')
        else:
            if request.method == 'POST':
                form =AccountTypeForm(request.POST, instance=request.user.profile)
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Welcome New User!')
                    return redirect('home')
            else:
                form = AccountTypeForm(instance=request.user.profile)
            return render(request, 'users/account_type.html', {'form':form})
    else:
        return render(request, 'mainapp/general_home.html')


def about(request):
    return HttpResponse('This is the about page!')
