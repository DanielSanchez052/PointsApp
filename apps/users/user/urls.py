from django.urls import path

from .api.views import RegisterUserView, GetRoleView

urlpatterns = [
    path('user/register/', RegisterUserView.as_view(), name='user_register'),
    path('user/role/', GetRoleView.as_view(), name='user_role'),
 ]