from allauth.account.forms import SignupForm
from django import forms
from .models import Startup, Slide, User
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=20, label='First name')
    last_name = forms.CharField(max_length=20, label='Last name')
    type = forms.ChoiceField(choices=User.TYPES, label='Укажите тип вашего аккаунта')
    name_of_company = forms.CharField(max_length=20, label='Назание организации', required=False)

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.new_user(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.type = self.cleaned_data['type']
        user.name_of_company = self.cleaned_data['name_of_company']

        adapter.save_user(request, user, self)
        self.custom_signup(request, user)

        setup_user_email(request, user, [])
        return user


class StartupForm(forms.ModelForm):

    class Meta:
        model = Startup
        exclude = ('creator', 'is_active')


class StartupImagesForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Slide
        fields = ['images']
