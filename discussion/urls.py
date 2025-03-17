from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat_view'),
    path('chat/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('forum/<int:forum_id>/', views.forum_detail, name='forum_detail'),
    path('groupe/<int:groupe_id>/', views.groupe_detail, name='groupe_detail'),
    path("chat/<int:chat_id>/message/", views.send_chat_message, name="send_chat_message"),
    path("forum/<int:forum_id>/message/", views.send_forum_message, name="send_forum_message"),
    path("groupe/<int:groupe_id>/message/", views.send_groupe_message, name="send_groupe_message"),
]