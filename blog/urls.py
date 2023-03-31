from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib import admin

from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), 
    path('accounts/login/', LoginView.as_view(), name='login'),

    #Extendions
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('admin/', admin.site.urls),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('', include('blog.urls')),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('drafts/', views.post_list, name='post_list'),
    path('post/outline/', views.post_outline, name='post_outline'),
]