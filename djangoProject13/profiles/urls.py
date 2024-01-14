from django.urls import path
from .views import profile_list, create_profile, profile_detail

urlpatterns = [
    path('', profile_list, name='profile_list'),
    path('create/', create_profile, name='create_profile'),
    path('profile/<int:profile_id>/', profile_detail, name='profile_detail'),
]

