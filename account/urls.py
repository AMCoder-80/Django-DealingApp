from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('test/', test),
    path('user/create/', UserCreation.as_view(), name='user_creation'),
    path('dealer/create/', DealerCreation.as_view(), name='dealer_creation'),
    path('login/', SignIn.as_view(), name="login"),
    path('logout/', SignOut.as_view(), name="logout"),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]