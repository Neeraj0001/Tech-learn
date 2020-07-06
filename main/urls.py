
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('logout/',views.logoutUser,name='logoutuser'),
    path('login_page/',views.login_page),
    path('Edit_profile.html/',views.E_profile,name='E_profile'),
    path('profile/<str:pk_test>/',views.profile,name='profile'),
    path('login_signup_page/',views.login_signup_page,name="login_signup"),
]
