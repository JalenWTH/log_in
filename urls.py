from django.urls import path
from log_in import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('log_in', views.log_in, name='log_in'),
]