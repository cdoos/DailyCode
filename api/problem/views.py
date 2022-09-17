from rest_framework.generics import CreateAPIView, DestroyAPIView
from src.models import Problem, Profile
from .serializers import ProblemCreateSerializer, ProblemSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProblemCreateAPIView(CreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'problem_id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        problem = serializer.save()
        return Response(ProblemSerializer(instance=problem).data)


class ProblemDestroyAPIView(DestroyAPIView):
    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'problem_id'

    def get_queryset(self):
        return Problem.objects.filter(profile=Profile.objects.get(user=self.request.user))
