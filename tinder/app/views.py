from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from .models import Startup, Slide
from .forms import StartupForm, StartupImagesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView, UpdateView, CreateView, ListView
from django.http import HttpResponseRedirect


User = get_user_model()


def main_page(request):
    return render(request, 'account/base.html')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['type', 'name_of_company']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse('users:detail', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _('Infos successfully updated')
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail', kwargs={'username': self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class StartupCreate(CreateView):
    model = Startup
    form_class = StartupForm
    template_name = 'app/startup_form.html'
    success_url = '/add-image/'

    def get_success_url(self):
        return f"/startups/{self.object.id}/add-image/"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


startup_create_view = StartupCreate.as_view()


class StartupCreateImage(CreateView):
    model = Slide
    form_class = StartupImagesForm
    template_name = 'app/slide_form.html'
    success_url = '/startups/'

    def get_success_url(self):
        return self.success_url

    def form_valid(self, form):
        self.object = None
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('images')
        startup_id = int(kwargs["id"])
        if form.is_valid():
            for f in files:
                instance = Slide(image=f, startup_id=startup_id)
                instance.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


startup_create_img_view = StartupCreateImage.as_view()


class StartupDetailView(DetailView):
    model = Startup
    slug_field = 'id'
    slug_url_kwarg = 'id'


startup_detail_view = StartupDetailView.as_view()


class StartupList(ListView):
    model = Startup


startup_list_view = StartupList.as_view()
