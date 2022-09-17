from django.contrib import admin
from src.models import User, Profile, Problem


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'password',
        'leetcode_username'
    )
    list_display_links = ['leetcode_username']
    search_fields = ['leetcode_username']
    fields = [
        'email',
        'password',
        'leetcode_username'
    ]


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'easy',
        'medium',
        'hard',
        'streak',
        'last_solved_date',
        'rating'
    )
    list_display_links = ['last_solved_date']
    list_filter = ['easy', 'medium', 'hard']
    fields = [
        'user',
        'easy',
        'medium',
        'hard',
        'streak',
        'last_solved_date',
        'rating'
    ]


@admin.register(Problem)
class ProblemModelAdmin(admin.ModelAdmin):
    list_display = (
        'problem_id',
        'title',
        'type',
        'solved',
        'profile'
    )
    list_filter = ['profile']
    fields = [
        'problem_id',
        'title',
        'type',
        'solved',
        'profile'
    ]
