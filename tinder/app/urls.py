from django.urls import path
from .views import main_page, user_detail_view, user_update_view, user_redirect_view, startup_create_view, \
    startup_create_img_view, startup_detail_view, startup_list_view

app_name = "users"
urlpatterns = [
    path('', main_page),
    path('users/redirect/', view=user_redirect_view, name='redirect'),
    path('users/update/', view=user_update_view, name='update'),
    path('users/<str:username>/', view=user_detail_view, name='detail'),
    path('startups/add/', view=startup_create_view, name='add-startup'),
    path('startups/<int:id>/add-image/', view=startup_create_img_view, name='add-img'),
    path('startups/<int:id>/', view=startup_detail_view, name='detail-startup'),
    path('startups/', view=startup_list_view, name='list-startup'),
]
