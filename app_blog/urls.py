from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('like/<int:pk>/', views.like_article, name='like_article'),
    path('comment/<int:pk>/', views.add_comment, name='add_comment'),
]
