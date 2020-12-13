from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class MyCustomSignupForm(SignupForm):
    fio = forms.CharField(max_length=20, label='ФИО')
    type = forms.ChoiceField(choices=(('CR', "Не выбрано"), ('Фонд', "Фонд"), ('Компания', "Компания"),
                                      ('Частный', "Частный")), label='Укажите тип вашего аккаунта')
    name_of_company = forms.CharField(max_length=20, label='Назание организации', required=False)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.fio = self.cleaned_data['fio']
        user.type = self.cleaned_data['type']
        user.name_of_company = self.cleaned_data['name_of_company']

        user.save()
        return user


# class UserChangeForm(admin_forms.UserChangeForm):
#     class Meta(admin_forms.UserChangeForm.Meta):
#         model = User
