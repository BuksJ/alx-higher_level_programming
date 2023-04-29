#!/usr/bin/python3
"""
This script takes two arguments, repository name and owner name,
and uses the GitHub API to print the 10 most recent
commits of the given repository by the given owner,
with their sha and author name
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

if response.status_code == 200:
    commits = response.json()[:10]
    for commit in commits:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
else:
    print("Error: Request failed with status code", response.status_code)
