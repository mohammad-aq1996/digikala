from django.urls import path
from django.contrib.auth import views as auth_view
from .views import RegisterView, WelcomeView

app_name = 'accounts_app'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='accounts_app/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
]
