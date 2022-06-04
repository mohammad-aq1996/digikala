from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


message = {
    'required': 'لطفا فیلد گذرواژه را وارد کنید'
}

class UserCreatForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "گذرواژه ها با هم تظابق ندارند",
    }
    password1 = forms.CharField(label='password', widget=forms.PasswordInput, error_messages=message)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput, error_messages=message)  
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        error_messages = {
            'username': {
                'required': 'لطفا فیلد نام کاربری را وارد کنید',
                'unique': 'یک نفر قبلا با این نام کاربری در سیستم ثبت نام کرده است',

                },
            'email': {
                'required': 'لطفا فیلد ایمیل را وارد کنید',
                'invalid': 'ایمیل وارد شده معتبر نمیباشد',
                'unique': 'این ایمیل قبلا در سیستم ثبت شده است',
                },
        }


class UserPersonalInfoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "receiver_name", "phone", "address", "post_id", "national_code", "card_number", "newsletter")
        widgets = {
            'newsletter':forms.CheckboxInput(),
        }
