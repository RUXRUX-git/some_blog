from django.urls import path

from sandbox import views

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('create_user/', views.create_user, name='create_user'),
    path('log_in/', views.log_in, name='log_in'),
    path('index/', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('chat/<str:username>/', views.chat),
    path('create_message/', views.create_message, name='create_message')
]
