from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import UserCreatForm


class RegisterView(CreateView):
    form_class = UserCreatForm
    success_url = reverse_lazy('accounts_app:welcome') # welcome
    template_name = 'accounts_app/register.html'


class WelcomeView(TemplateView):
    template_name = 'accounts_app/welcome.html'