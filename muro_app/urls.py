from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('deletemsg', views.delete_msg),
    path('deletecmt', views.delete_cmt),
    path('content', views.content),
]