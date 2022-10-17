from django.urls import path, include
from accounts.views import RegistrationView, LogoutView, LoginView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login')
]