from django.urls import path
from authenticate.views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name="logout"),
    path('register/', register_user, name="register"),
    path('user/', get_users),
]
