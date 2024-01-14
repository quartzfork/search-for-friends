from django.urls import path
from .views import profile_list, create_profile, profile_detail, edit_profile, delete_profile

urlpatterns = [
    path('', profile_list, name='profile_list'),
    path('create/', create_profile, name='create_profile'),
    path('profile/<int:profile_id>/', profile_detail, name='profile_detail'),
    path('edit_profile/<int:profile_id>/', edit_profile, name='edit_profile'),
    path('delete_profile/<int:profile_id>/', delete_profile, name='delete_profile'),
]

