from rest_framework.routers import DefaultRouter

from .viewsets import ProfileUserViewset

router = DefaultRouter()
router.register(r'profile', ProfileUserViewset, basename='profile_user_router')
