from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateAPIView
from src.models import Profile
from .serializers import ProfileSerializer, ProfileUpdateSerializer, ProfileTopPlaceSerializer
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter


class ProfileAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    lookup_field = 'user__leetcode_username'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProfileSerializer
        else:
            return ProfileUpdateSerializer


class ProfileTopAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['rating', 'streak']


class ProfileTopPlaceAPIView(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileTopPlaceSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['rating', 'streak']

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        queryset = self.filter_queryset(self.get_queryset())
        rank = 1
        for profile in queryset:
            if profile.user.leetcode_username == serializer.data['leetcode_username']:
                return Response({'place': rank})
            rank += 1

        return Response(status=404)
