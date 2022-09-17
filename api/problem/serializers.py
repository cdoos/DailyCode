from rest_framework import serializers
from src.models import Profile
from src.models import Problem
from external_api.lcid import get_leetcode_problem


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = (
            'problem_id',
            'title',
            'type',
            'solved'
        )


class ProblemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('problem_id', )

    def create(self, validated_data):
        problem_id = validated_data.pop('problem_id')
        data = get_leetcode_problem(problem_id)
        data['profile'] = Profile.objects.get(user=self.context.get('request').user)
        problem = Problem.objects.create(**data)
        return problem
