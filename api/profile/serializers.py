from rest_framework import serializers
from src.models import Profile
from api.problem import ProblemSerializer
from rest_framework.validators import ValidationError


class ProfileSerializer(serializers.ModelSerializer):
    leetcode_username = serializers.SerializerMethodField()
    problems = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'leetcode_username',
            'first_name',
            'last_name',
            'easy',
            'medium',
            'hard',
            'streak',
            'last_solved_date',
            'photo',
            'problems',
            'rating'
        )

    def get_leetcode_username(self, obj):
        return obj.user.leetcode_username

    def get_problems(self, obj):
        return ProblemSerializer(obj.problems, many=True).data


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'photo'
        )


class ProfileRatingSerializer(serializers.ModelSerializer):
    leetcode_username = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = (
            'leetcode_username',
            'photo',
            'rating'
        )


class ProfileStreakSerializer(serializers.ModelSerializer):
    leetcode_username = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = (
            'leetcode_username',
            'photo',
            'streak'
        )


class ProfileTopPlaceSerializer(serializers.Serializer):
    leetcode_username = serializers.CharField()

    def validate(self, attrs):
        leetcode_username = attrs['leetcode_username']
        profile = Profile.objects.filter(user__leetcode_username=leetcode_username)
        if not profile:
            raise ValidationError({'leetcode_username': 'Invalid leetcode username'})
        return attrs
