from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from django_countries.fields import CountryField
from .choice import Account_Choice
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)
    number = models.IntegerField(null=True)
    website = models.URLField( null=True)
    account_type = models.CharField(max_length=10, choices=Account_Choice, default='')
    profile_over = models.TextField(null=True, max_length=3000)

    # country = CountryField(blank_label='(select country)', null=True)
    


    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=3000)
    proposal = models.ManyToManyField(User,related_name='post_proposal')

    def __str__(self):
        return f"{self.title} by {self.owner.username}"

    class Meta:
        ordering = ['title']


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
 
    