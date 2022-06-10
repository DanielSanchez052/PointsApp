from django.urls import path

from .api.views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user_register') 
 ]