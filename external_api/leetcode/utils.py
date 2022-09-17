import requests
import json
from datetime import datetime
from .constants import *


def get_solved_problems(leetcode_username):
    QUERY_PROFILE['variables']['username'] = leetcode_username
    response = requests.post(url=URL, headers=HEADERS, data=json.dumps(QUERY_PROFILE)).json()
    if 'errors' in response:
        raise ValueError(f'Leetcode username {leetcode_username} does not exist')
    response = response['data']['matchedUser']['submitStats']['acSubmissionNum']
    data = {types['difficulty'].lower(): types['count'] for types in response if types['difficulty'] != 'All'}
    return data


def get_last_submission_date(leetcode_username):
    QUERY_RECENT_SUBMISSION['variables']['username'] = leetcode_username
    response = requests.post(url=URL, headers=HEADERS, data=json.dumps(QUERY_RECENT_SUBMISSION)).json()
    if 'errors' in response:
        raise ValueError(f'Leetcode username {leetcode_username} does not exist')
    response = response['data']['recentAcSubmissionList']
    if len(response) == 0:
        return None
    return datetime.fromtimestamp(int(response[0]['timestamp'])).astimezone()
