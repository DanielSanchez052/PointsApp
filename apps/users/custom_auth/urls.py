from django.urls import path, include, re_path

from apps.users.custom_auth.api.views import LoginView, LogoutView, ChangePasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name="authentication_login"),
    path('logout/', LogoutView.as_view(), name="authentication_logout"),
    path('change_password/', ChangePasswordView.as_view(),
         name="authentication_change_password"),
    re_path(r'^password_reset/', include('django_rest_passwordreset.urls',
            namespace='password_reset')),
]
