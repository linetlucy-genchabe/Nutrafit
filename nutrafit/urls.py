from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'register/$',views.register ),
    url(r'accounts/login/$',views.user_login, name='login'),
    url(r'logout/$',views.signout),
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),
    url(r'^category/(\w+)', views.get_category,name='get_category'),

    url(r'^add_post_comment/(\d+)$',views.comment,name='comment'),
    url(r'^like_post/(\d+)$',views.like_post,name='like_post'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^single/post/(\d+)$', views.single_post, name='single_post'),
    url(r'^search/', views.search_posts, name='search_results'),
    # url(r'^post/(\d+)', views.get_post, name='business_results'),
   
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)