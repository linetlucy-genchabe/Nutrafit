from django import forms
from .models import *
from django.contrib.auth.models import User


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		
		exclude = ['user','post',]

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['Author', 'pub_date', 'author_profile', ]
        widgets = {
          'post': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }