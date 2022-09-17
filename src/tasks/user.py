from config import celery_app
from src.models import Profile
from external_api.leetcode import (
    get_solved_problems,
    get_last_submission_date
)


@celery_app.task()
def update_profiles_from_leetcode_api():
    profiles = Profile.objects.all()
    for profile in profiles:
        data = get_solved_problems(profile.user.leetcode_username)
        data['last_solved_date'] = get_last_submission_date(profile.user.leetcode_username)
        data['rating'] = data['hard'] * 7 + data['medium'] * 3 + data['easy'] * 1
        Profile.objects.filter(user__leetcode_username=profile.user.leetcode_username).update(**data)
