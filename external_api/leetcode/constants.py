URL = 'https://leetcode.com/graphql'

HEADERS = {
    "content-type": "application/json",
    "origin": "https://leetcode.com",
    "referer": "https://leetcode.com/problemset/all/"
}

QUERY_PROFILE = {
    "operationName": "getUserProfile",
    "variables": {"username": ""},
    "query": '''\
        query getUserProfile($username: String!) {
            matchedUser(username: $username) {
                username
                submitStats: submitStatsGlobal {
                    acSubmissionNum {
                        difficulty
                        count
                        submissions
                    }
                }
            }
        }
    ''',
}

QUERY_RECENT_SUBMISSION = {
    "operationName": "recentAcSubmissions",
    "variables": {"username": "", "limit": 1},
    "query": '''\
        query recentAcSubmissions($username: String!, $limit: Int!) {
            recentAcSubmissionList(username: $username, limit: $limit) {
                timestamp
            }
        }
    ''',
}
