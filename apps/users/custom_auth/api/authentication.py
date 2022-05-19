from rest_framework import authentication

def default_user_authentication_rule(user):
    return user is not None and user.is_active


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return