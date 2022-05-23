from django.urls import path
from django.contrib.auth import views as auth_view
from .views import RegisterView, WelcomeView, ProfileView, PassChangeView, ProfilePersonalInfoView, ProfileEditPersonalInfoView

app_name = 'accounts_app'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='accounts_app/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password/change/', PassChangeView.as_view(), name='password_change'),
    path('password/change/done/', 
        auth_view.PasswordChangeDoneView.as_view(template_name='accounts_app/password-change-done.html'), 
        name="password_change_done"),
    path('personal-info/', ProfilePersonalInfoView.as_view(), name='personal-info'),
    path('profile/checkout/<int:pk>/', ProfileEditPersonalInfoView.as_view(), name='edit-profile'),
]
