from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .forms import UserCreatForm


class RegisterView(CreateView):
    form_class = UserCreatForm
    success_url = reverse_lazy('accounts_app:welcome') # welcome
    template_name = 'accounts_app/register.html'


class WelcomeView(TemplateView):
    template_name = 'accounts_app/welcome.html'


class ProfileView(TemplateView):
    template_name = 'accounts_app/profile.html'


class PassChangeView(PasswordChangeView):
    template_name='accounts_app/password-change.html'
    success_url = reverse_lazy('accounts_app:password_change_done')


