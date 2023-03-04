from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import UserLoginView, UserRegistrationView, UserProfileView, logout

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),
]
