from django.urls import path
from . import views

urlpatterns = [
    path('todays-msg/', views.go_todays_msg, name="todays-msg"),
    path('new-post/', views.create_new_post, name="new-post"),
    path('completed/', views.completed, name="completed"),
    path('upvote/', views.upvote, name='upvote'),
    # path('favorite/', views.favorite, name='favorite'),
]