from posixpath import basename
from django.urls import path,include

from .api.views import RegisterUserView

urlpatterns = [
    path('user/register/', RegisterUserView.as_view(), name='user_register'),
 ]