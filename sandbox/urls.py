from django.urls import path

from sandbox import views

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('create_user/', views.create_user, name='create_user'),
    path('log_in/', views.log_in, name='log_in')
]
