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
    # url(r'^new/business$', views.new_post, name='new-post'),


    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^search/', views.search_posts, name='search_results'),
    # url(r'^post/(\d+)', views.get_post, name='business_results'),
   
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)