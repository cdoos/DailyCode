from django.urls import path
from api.auth import UserAPIView
from api.profile import (
    ProfileAPIView,
    ProfileTopAPIView,
    ProfileTopPlaceAPIView
)
from api.problem import (
    ProblemCreateAPIView,
    ProblemDestroyAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path(r'auth/register/', UserAPIView.as_view(), name='register'),
    path(r'auth/login/', TokenObtainPairView.as_view(), name='auth'),
    path(r'top/', ProfileTopAPIView.as_view(), name='top'),
    path(r'profile/<user__leetcode_username>/', ProfileAPIView.as_view(), name='profile'),
    path(r'place/', ProfileTopPlaceAPIView.as_view(), name='profile_place'),
    path(r'problem/', ProblemCreateAPIView.as_view(), name='problem_create'),
    path(r'problem/<int:problem_id>/', ProblemDestroyAPIView.as_view(), name='problem_delete')
]
