from django.contrib import admin
from .models import User
from .models import Slide
from .models import Startup
from .models import InvestorsChoice


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    pass


@admin.register(Startup)
class StartUpAdmin(admin.ModelAdmin):
    pass


@admin.register(InvestorsChoice)
class InvestorsChoiceAdmin(admin.ModelAdmin):
    pass


