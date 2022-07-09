from django.contrib.auth.models import AnonymousUser

from rest_framework.permissions import BasePermission

class RegisterUserPermission(BasePermission):
    message = "You do not have permission to perform this action."
    
    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_anonymous or request.user.is_superuser or request.user.is_staff))