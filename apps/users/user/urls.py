from django.urls import path

from .api.views import RegisterUserView, GetRoleView, GetCities, GetDepartments, GetCounties, GetIdentificationTypes, GetProfileStatus

urlpatterns = [
    path('user/register/', RegisterUserView.as_view(), name='user_register'),
    path('user/role/', GetRoleView.as_view(), name='user_role'),
    path('user/city/', GetCities.as_view(), name='user_cities'),
    path('user/department/', GetDepartments.as_view(), name='user_departments'),
    path('user/country/', GetCounties.as_view(), name='user_countries'),
    path('user/identification_type/', GetIdentificationTypes.as_view(), name='user_identification_types'),
    path('profile/profile_status/', GetProfileStatus.as_view(), name='user_profile_status'),
 ] 