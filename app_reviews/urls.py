from django.urls import path
from . import views

app_name = 'app_reviews'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('like/<int:review_id>/', views.like_review, name='like_review'),
]
