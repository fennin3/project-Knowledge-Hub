from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile, Post
from phonenumber_field.modelfields import PhoneNumberField
from .choice import Account_Choice


options = [('Tutor', 'Tutor'), ('Student','Student')]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    profile_over = forms.CharField(label='Profile Overview', widget=forms.Textarea())
    profile_pic = forms.ImageField(label='Profile Picture', allow_empty_file=True)
    number = forms.IntegerField(label='Phone Number')
    class Meta:
        model = Profile
        fields = '__all__'


class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['account_type']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']