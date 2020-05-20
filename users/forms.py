from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
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

# class EditProfileForm(UserChangeForm):
#     email = forms.EmailField()
    # profile_pic = forms.ImageField(label='Profile Picture')
    # website = forms.URLField(null=True)
    # number = forms.IntegerField()
    # account_type = forms.ChoiceField(label='Account Type', choices=Account_Choice, initial="", widget=forms.Select(), required=True)
    # profile_over = forms.CharField(widget=forms.Textarea())

    # class Meta:
    #     model = User
    #     fields = (
    #         'email',
    #         'first_name',
    #         'last_name',
    #         'password'
    #     )



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['account_type']
