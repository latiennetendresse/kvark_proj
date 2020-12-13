from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


# Наследуем модель Юзера
class User(AbstractUser):
    CREATOR = 'CR'
    FUND = 'FN'
    COMPANY = 'CM'
    PRIVATE = 'PR'
    TYPES = [
        (CREATOR, 'Не выбрано'),
        (FUND, 'Фонд'),
        (COMPANY, 'Компания'),
        (PRIVATE, 'Частный'),
    ]
    fio = models.CharField(max_length=50, default='unknown')
    email = models.EmailField(verbose_name='email')
    type = models.CharField(max_length=10, choices=TYPES, default=CREATOR, verbose_name='type')
    name_of_company = models.CharField(max_length=20, verbose_name='name of company', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={"username": self.username})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


# Создание модели стартапа
class Startup(models.Model):
    name = models.CharField("Название", max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')
    desc = models.CharField("Описание", max_length=500)
    pitch_deck = models.FileField("Презентация", upload_to='pitch_decks/%Y/%m/%d/')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='InvestorsChoice',
                                     through_fields=('startup', 'user'))

    class Meta:
        verbose_name = 'Стартап'
        verbose_name_plural = "Стартапы"

    def __str__(self):
        return self.name


class Slide(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')


# Промежуточная таблица отобранных проектов
class InvestorsChoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    response = models.BooleanField("Реакция")




