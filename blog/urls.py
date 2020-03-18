from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdaetView, PostDeleteView, UserPostListView
from  .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update',PostUpdaetView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about,name='blog-about'),
    path('services/',views.services,name='blog-services'),
]
