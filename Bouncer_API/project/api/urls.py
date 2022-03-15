from django.urls import path
from api.views.register_view import RegisterView
from api.views.login_views import LoginView
from api.views.forget_password import ForgotPasswordView
from .views.reset_password import PasswordResetAPI
from api.views.logout_views import logout_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot_password/', ForgotPasswordView.as_view(),
         name="forgot-password"),
    path('password-reset/<otp>/',
         PasswordResetAPI.as_view(), name='password-reset-token-check'),
    path('logout/', logout_view, name='logout')
]
