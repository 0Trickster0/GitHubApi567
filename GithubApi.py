import json
import requests


def parse_github_info(user_name: str):
    name_url: str = f'https://api.github.com/users/{user_name}/repos'
    response = requests.get(name_url)
    json_info = json.loads(response.text)
    for repo in json_info:
        if type(repo) == str:
            yield 'The API rate limit is exceeded. Please try it later.'
        repo_name = repo['name']
        commits_url: str = f'https://api.github.com/repos/{user_name}/{repo_name}/commits'
        res = requests.get(commits_url)
        j_info = json.loads(res.text)
        if type(j_info) == list:
            yield f'Repo: {repo_name}, Number of commits: {len(j_info)}'
        else:
            yield f'Repo: {repo_name}, Number of commits: 0'


if __name__ == '__main__':
    for info in parse_github_info('0Trickster0'):
        print(info)
