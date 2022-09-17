from rest_framework.generics import CreateAPIView
from src.models import User
from .serializers import UserCreateSerializer


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
