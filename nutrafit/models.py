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
        return str(self.user)
    
    # def __str__(self):
    #     return f"{self.user}, {self.bio}, {self.photo}"
    
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
    
    
    def save_posts(self):
        self.save()
    
    def delete_posts(self):
        self.delete()
        
    @classmethod
    def get_allposts(cls):
        posts = cls.objects.all()
        return posts
    
    @classmethod
    def search_posts(cls, search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts
    
    @classmethod
    def get_by_Category(cls, categories):
        posts = cls.objects.filter(category__name__icontains=categories)
        return posts
    
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

class Likes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    post_id= models.ForeignKey(Posts,on_delete=models.CASCADE)

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
       

	    
