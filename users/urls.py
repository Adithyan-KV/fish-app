from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup_page'),
    path('messages', views.info_messages, name='messages_page')
]
