# Django
from django.urls import path
# Views
from . import views

app_name ='users_app'

urlpatterns = [
   path(
    'register/',
    views.UserRegisterView.as_view(),
    name='register'
   ),
   path(
       "login/",
       views.LoginUser.as_view(),
       name="user-login"
   ),
   path(
       "logout/",
       views.LogoutUser.as_view(),
       name="user-logout"
   ),
   path(
    'update/<pk>/',
    views.UpdateUSer.as_view(),
    name='user-update'
   ),
   path(
    'update-password/',
    views.UpdatePasswordUser.as_view(),
    name='user-update-password'
   ),
   path(
    'verifications/<pk>/',
    views.CodeVerificationsView.as_view(),
    name='user-verification'
   ),
]
