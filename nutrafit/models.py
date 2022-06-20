from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404


# Create your models here.
   
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    
    def __str__(self):
        return self.name


    def save_category(self):
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('image')
    

    def save_profile(self):
        self.save()
        
        

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return f"{self.user}, {self.bio}, {self.photo}"
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
            
        
class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    pic = CloudinaryField('pic')
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    admin_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    
    
    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()
        
    @classmethod
    def get_allposts(cls):
        post = cls.objects.all()
        return post
    
    @classmethod
    def search_posts(cls, search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post
    
    @classmethod
    def get_by_Category(cls, categories):
        post = cls.objects.filter(category__name__icontains=categories)
        return post
    
    @classmethod
    def get_posts(request, id):
        try:
            post = Posts.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return post
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Posts'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
        post = models.ForeignKey(Posts, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        content = models.TextField(max_length=160)

        def __str__(self):
            return self.content

        def save_comment(self):
            self.save()

        def delete_comment(self):
            self.delete()



       

	    
