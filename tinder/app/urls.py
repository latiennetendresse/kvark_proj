from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('', main_page),
    path('users/redirect/', view=user_redirect_view, name='redirect'),
    path('users/update/', view=user_update_view, name='update'),
    path('users/<str:username>/', view=user_detail_view, name='detail'),
    path('startups/add/', view=startup_create_view, name='add'),
    path('add-image/', view=startup_createimg_view, name='add-img'),
    path('startups/<int:id>/', view=startup_detail_view, name='detail-startup'),

]
