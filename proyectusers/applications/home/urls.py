# Django
from django.urls import path
# Views
from . import views

app_name = 'home_app'

urlpatterns = [
   path(
    'panel/',
    views.HomePage.as_view(),
    name='user-panel'
   ),
]
