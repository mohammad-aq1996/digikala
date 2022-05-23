from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreatForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class UserPersonalInfoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "receiver_name", "phone", "address", "post_id", "national_code", "card_number", "newsletter")
        widgets = {
            'newsletter':forms.CheckboxInput(),
        }
