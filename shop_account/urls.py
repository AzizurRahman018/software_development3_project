from django.urls import path
from .views import *
urlpatterns = [
path('login/',LOGIN,name='login'),
path('reg/',Reg,name='reg'),
path('reset/',Reset,name='reset'),
path('logout/',LOGOUT,name='logout'),
path('user_desh/',user_desh,name='user_desh')
]
