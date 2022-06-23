from gc import get_objects
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.templatetags.static import static
# from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from .email import send_welcome_email
# Create your views here.



# Create your views here.

def index(request):
    posts = Posts.objects.all()

    if request.method == 'POST':
        letterform = NewsLetterForm(request.POST)
        if letterform.is_valid():
            name = letterform.cleaned_data['your_name']
            email = letterform.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('index')
            #.................
    else:
            letterform = NewsLetterForm()
    
    return render(request, 'index.html', {'posts':posts, 'letterform':letterform})



def contact(request):
    
    
    return render(request, 'contact.html')

def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome , you are now logged in")
            return redirect ("index")
    return render(request, 'registration/login.html')




def register(request):
    
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"confirm your passwords")
            return redirect('/register')
        
        new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        
        new_user.save()
        
        return render(request,'registration/login.html')
    return render(request, 'registration/registration.html')

def signout(request):
    logout(request)
    messages.success(request,"You have logged out")
           
    return redirect("/")


@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    
    profile = Profile.objects.get(user=request.user)
    # profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)   
        if form.is_valid():
            current_user=current_user
            profile = form.save(commit=False)
            profile.save()
            form.save()
            return redirect('profile')
            
    else:
        form = ProfileUpdateForm()


    return render(request, 'registration/profile.html', {"form":form})




# @login_required(login_url='/accounts/login/')
# def comments(request,id):
	
# 	post = get_objects(Posts,id=id)	
# 	current_user = request.user
# 	print(post)

# 	if request.method == 'POST':
# 		form = CommentForm(request.POST)

# 		if form.is_valid():
# 			comment = form.save(commit=False)
# 			comment.user = current_user
# 			comment.post = post
# 			comment.save()
# 			return redirect('index')
# 	else:
# 		form = CommentForm()

# 	return render(request,'comment.html',{"form":form}) 

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = request.user.profile
   

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.author_profile = profile

            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'new-post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def search_posts(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Posts.search_posts(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"businesses": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

def get_category(request,category):
    category_results = Category.objects.all()
    
    category_result = Posts.objects.filter(post_category__name = category)
    return render(request,'index.html',{'my_posts':category_result,'category_results':category_results,})

@login_required(login_url='login')
def single_post(request,post_id):
    post = Posts.objects.get(id=post_id)
    current_user = request.user
    profile = request.user.profile
    user =User.objects.get(username=current_user.username)
    comments = Comment.objects.filter(post_id=post_id)
    likes_count = Likes.objects.filter(post_id=post_id).count()
    liked = False

    try:

        like = Likes.objects.filter(post_id=post_id, user_id=user.id)

        if like:
            liked = True
        else:
            liked = False

    except Likes.DoesNotExist:
        print('')
    cxt={
        'post':post,
        'comments':comments,
        'likes_count':likes_count,
        'liked':liked,
        'profile':profile,
    }
    return render(request,'single_post.html',cxt)


def comment(request, post_id):

    current_user = request.user
    
    profile = request.user.profile
    user = User.objects.get(username=current_user.username)
    post = Posts.objects.get(id=post_id)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            # form.save()
            comment = form.save(commit=False)

            comment.user_id = user.id
            comment.post_id = post.id
            comment.Author = current_user
            comment.author_profile = profile
            comment.save()

            return redirect('/')
        else:
            form = CommentForm()

    ctx = {
        'form': form,
        'post': post
    }

    return render(request, 'comment.html', ctx)


def like_post(request, post_id):

    current_user = request.user
    user = User.objects.get(username=current_user.username)
    posts = Posts.objects.get(id=post_id)

    try:

        like = Likes.objects.filter(post_id=post_id, user_id=user.id)

        if like:
            like.delete()
        else:
            Likes.objects.create(
                user_id=user,
                post_id=posts.id
            )

    except Likes.DoesNotExist:
        print('')

    return redirect('single_post', post_id=posts.id)
