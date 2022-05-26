from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from store_app.models import Cart
from .models import Users
from .forms import UserCreatForm, UserPersonalInfoForm


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


class ProfilePersonalInfoView(TemplateView):
    template_name = 'accounts_app/profile-personal-info.html'


class ProfileEditPersonalInfoView(LoginRequiredMixin, UpdateView):
    model = Users
    form_class = UserPersonalInfoForm
    success_url = reverse_lazy('accounts_app:profile')
    template_name = 'accounts_app/checkout.html'


class ProfileOrderListView(TemplateView):
    template_name = 'accounts_app/profile-orders.html'
