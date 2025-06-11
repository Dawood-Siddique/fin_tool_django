from django.urls import path
from .views import (
    LoginPageView,
    LogoutView,
    RegisterPageView
)

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login-page'),
    path('logout/', LogoutView.as_view(), name='logout-page'),
    path('register/', RegisterPageView.as_view(), name='register-page')
]
