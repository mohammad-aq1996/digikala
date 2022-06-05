from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


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
    phone_error_message = {
        'max_length': 'شماره تلفن باید 11 رقم باشد',
        'min_length': 'شماره تلفن باید 11 رقم باشد',
    }
    post_error_message = {
        'max_length': 'کد پستی باید 10 رقم باشد',
        'min_length': 'کد پستی باید 10 رقم باشد',
    }
    national_code_error_message = {
        'max_length': 'کد ملی باید 10 رقم باشد',
        'min_length': 'کد ملی باید 10 رقم باشد',
    }
    card_number_error_message = {
        'max_length': 'شماره کارت باید 16 رقم باشد',
        'min_length': 'شماره کارت باید 16 رقم باشد',
    }
    phone = forms.CharField(error_messages=phone_error_message, max_length=11, min_length=11, required=False)
    post_id = forms.CharField(error_messages=post_error_message, max_length=10, min_length=10, required=False)
    national_code = forms.CharField(error_messages=national_code_error_message, max_length=10, min_length=10, required=False)
    card_number = forms.CharField(error_messages=card_number_error_message, max_length=16, min_length=16, required=False)
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "receiver_name", "phone", "address", "post_id", "national_code", "card_number", "newsletter")
        widgets = {
            'newsletter':forms.CheckboxInput(),
        }
       

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', None)
        if phone:
            try:
                int(phone)
            except (ValueError, TypeError):
                raise ValidationError('شماره تلفنی که وارد کرده اید معتبر نمیباشد')
        return phone

    def clean_post_id(self):
        post_id = self.cleaned_data.get('post_id', None)
        if post_id:
            try:
                int(post_id)
            except (ValueError, TypeError):
                raise ValidationError('کد پستی که وارد کرده اید معتبر نمیباشد')
        return post_id

    def clean_national_code(self):
        national_code = self.cleaned_data['national_code']
        if national_code:
            try:
                int(national_code)
            except (ValueError, TypeError):
                raise ValidationError('کد ملی که وارد کرده اید معتبر نمیباشد')
        return national_code

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number', None)
        if card_number:
            try:
                int(card_number)
            except (ValueError, TypeError):
                raise ValidationError('شماره کارتی که وارد کرده اید معتبر نمیباشد')
        return card_number