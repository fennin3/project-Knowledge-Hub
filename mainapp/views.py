from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from users.forms import AccountTypeForm, PostForm
from django.contrib import messages
from users.models import Post
from django.contrib.auth.models import User
from django.views.generic import DetailView


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.account_type == 'Tutor' or request.user.profile.account_type == 'Student':
            posts = Post.objects.all()
            users = User.objects.filter(profile__account_type="Tutor")
            return render(request, 'mainapp/index.html', {'posts':posts, 'users':users})
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

def post_request(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.owner = request.user
            fm.save()
            form.save()
            messages.success(request, f'Your request was posted!')
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostForm()
    return render(request, 'mainapp/post_page.html', {'form':form})


class PostDetailView(DetailView):
	model = Post
	template_name = 'mainapp/post.html'
