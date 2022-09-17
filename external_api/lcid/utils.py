import requests
from .constants import URL


def get_leetcode_problem(problem_id):
    response = requests.get(url=f'{URL}{problem_id}')
    if response.status_code != 200:
        raise ValueError(f'The title for problem id {problem_id} not found')
    response = response.json()
    data = {
        'problem_id': problem_id,
        'title': response['title'],
        'titleSlug': response['titleSlug'],
        'type': response['difficulty']
    }
    return data
